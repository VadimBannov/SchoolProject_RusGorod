import telebot
import json
import time
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import *
from config import *

# Токен и класс GPT
bot = telebot.TeleBot(BOT_TOKEN)
prepare_db()

# Выведение ошибок с помощью Logging
logging.basicConfig(
    level=logging.ERROR,
    filename="log_file.txt",
    filemode="a"
)

# -------------------- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ --------------------

# Функция для создания кнопок
def create_markup(labels, row_width=1):
    markup = InlineKeyboardMarkup(row_width=row_width)
    markup.add(*(InlineKeyboardButton(text=l, callback_data=l) for l in labels))
    return markup

def locked(uid):
    return get_data_for_user(uid)["right_answer"] is None

# Безопасно распарсит JSON-строку в список. Возвращает [] при пустом/некорректном входе.
# noinspection PyBroadException
def safe_list(value):
    if not value:
        return []
    if isinstance(value, list):
        return value
    try:
        return json.loads(value)
    except Exception:
        return []


# Проверяет ли есть пользователь в базе данных
def check_user(callback):
    uid = callback.from_user.id
    if not is_value_in_table(DB_TABLE_USERS_NAME, "user_id", uid):
        initial_insertion([uid, callback.from_user.first_name])
        bot.send_message(uid, "Произошла перезагрузка. Вы в главном меню.")
        start(callback)
        return False
    return True

# -------------------- ИГРОВАЯ ЛОГИКА -------------------

def next_round(uid):
    data = get_data_for_user(uid)
    held = safe_list(data["cities_held"])

    result = uploading_photos_buttons(held, data["mode"], data["submode"])
    if result is None:
        update_row_value(uid, "right_answer", None)
        return None

    photo, hint1, options, answer, information = result

    held.append(answer)
    update_row_value(uid, "cities_held", json.dumps(held, ensure_ascii=False))
    update_row_value(uid, "right_answer", answer)
    update_row_value(uid, "hint", hint1)
    update_row_value(uid, "documentation", information)

    return photo, options

def send_question(uid, text, separation, callback_id):
    result = next_round(uid)
    if not result:
        bot.send_message(uid, "Завершение игры.", reply_markup=create_markup(["🚪 Выйти"]))
        bot.answer_callback_query(callback_id)
        return

    if get_data_for_user(uid)["score"] > 1:
        update_row_value(uid, "gauge", "Верно✅")

    photo, options = result
    data = get_data_for_user(uid)

    buttons = options + (["💡 Подсказка"] if data["mode"] == "City" else []) + ["🏁 Завершить"]

    if not data["gauge"] is None:
        indicator = f'{data["gauge"]}\n{data["score"]}'
    else:
        indicator = f"{data['score']}"

    bot.send_photo(
        uid,
        photo,
        caption=f"{indicator}. {text}",
        reply_markup=create_markup(buttons, separation)
    )
    bot.answer_callback_query(callback_id)

def start_game(callback, mode, submode=None):
    uid = callback.from_user.id

    update_row_value(uid, "submode", submode)
    update_row_value(uid, "score", 1)
    update_row_value(uid, "cities_held", "[]")
    update_row_value(uid, "state", "Game")

    titles = {
        "City": "Укажите верный город!",
        "Gerb": "Укажите верный герб!",
        "Attractions": "Укажите верную достопримечательность!"
    }

    separation = {
        "City": 2,
        "Gerb": 2,
        "Attractions": 1
    }

    send_question(uid, titles[mode], separation[mode], callback.id)


# -------------------- МЕНЮ --------------------

@bot.message_handler(commands=["start"])
def start(message):
    uid = message.from_user.id
    if not is_value_in_table(DB_TABLE_USERS_NAME, "user_id", uid):
        initial_insertion([uid, message.from_user.first_name])

    reset_table_value(uid)

    bot.send_message(
        message.from_user.id,
        "🇷🇺 РусГород\nВыберите режим:",
        reply_markup=create_markup([
            "🏙 Города",
            "🛡 Гербы",
            "🏛 Достопримечательности",
            "🎲 Случайный режим",
            "⭐ Список лидеров",
            "ℹ️ О проекте"
        ], 1)
    )

@bot.message_handler(commands=["help"])
def support(message):
    uid = message.from_user.id

    bot.send_message(uid, text=DOCUMENTATION)

@bot.message_handler(commands=["leader"])
def leader_command(message):
    uid = message.from_user.id

    top = get_most_points()

    if not top:
        bot.send_message(uid, "Таблица лидеров пуста.")
        return

    text = "\n".join(
        f"{i}. {name} — {points}"
        for i, (name, points) in enumerate(top, 1)
    )

    bot.send_message(uid, f"🏆 Таблица лидеров:\n\n{text}")


@bot.callback_query_handler(func=lambda c: c.data == '⭐ Список лидеров')
def leader(callback):
    uid = callback.from_user.id

    if not check_user(callback):
        return

    top = get_most_points()

    if not top:
        bot.send_message(uid, "Таблица лидеров пуста.")
        bot.answer_callback_query(callback.id)
        return

    text = "\n".join(
        f"{i}. {name} — {points}"
        for i, (name, points) in enumerate(top, 1)
    )

    bot.send_message(uid, f"🏆 Таблица лидеров:\n\n{text}")
    bot.answer_callback_query(callback.id)


@bot.callback_query_handler(func=lambda c: c.data == 'ℹ️ О проекте')
def documentation(callback):
    uid = callback.from_user.id

    if not check_user(callback):
        return

    bot.send_message(uid, text=DOCUMENTATION)
    bot.answer_callback_query(callback.id)

@bot.callback_query_handler(func=lambda c: c.data == 'ℹ️ О режимах')
def documentation(callback):
    uid = callback.from_user.id
    mode = get_data_for_user(uid)["mode"]

    if not check_user(callback):
        return
    if mode == "City":
        bot.send_message(uid, text=f"Режимы городов:\n"
                                   f"🎮 Аркадный — в этом режиме игра имеет завершение. В ходе прохождения игры вы сможете увидеть уникальный город, который в раунде не повторится. Количество попыток не ограничены, однако очки рейтинга не будут учитываться.\n"
                                   f"🏆 Рейтинг — бесконечный режим. В этом режиме не предоставляется возможность совершить ошибки. За каждое успешное действие начисляются рейтинговые очки. Режим предназначен для соревнований между игроками.")
        bot.answer_callback_query(callback.id)
        return
    elif mode == "Attractions":
        bot.send_message(uid, text=f"Режимы достопримечательности:\n"
                                   f"🎮 Аркадный — в этом режиме вопросы идут последовательно без географическо-исторической справки и интересных фактов. Режим предназначен для укрепления знаний о достопримечательности.\n"
                                   f"✈️ Экскурсионный — учебный режим, в котором при каждом верном ответе будет давать интересные факты, состоящие из исторических и географических сведений о пройденной достопримечательности. Таким образом, можно получить много интересной информации о различных уголках России.")
        bot.answer_callback_query(callback.id)
        return

    # -------------------- ЗАПУСК РЕЖИМОВ --------------------

@bot.callback_query_handler(func=lambda c: c.data == "🏙 Города")
def city_menu(callback):
    uid = callback.from_user.id
    state = get_data_for_user(uid)["state"]

    update_row_value(uid, "mode", "City")
    if not check_user(callback):
        return
    if state != "Menu":
        bot.answer_callback_query(callback.id, "Сначала завершите текущую игру!", show_alert=True)
        return

    bot.edit_message_text(
        "Выберите режим:",
        callback.message.chat.id,
        callback.message.message_id,
        reply_markup=create_markup(["🎮 Аркадный", "🏆 Рейтинг", "ℹ️ О режимах", "🚪 Выйти"], 1)
    )
    bot.answer_callback_query(callback.id)


@bot.callback_query_handler(func=lambda c: c.data == "🎮 Аркадный")
def arcade(callback):
    uid = callback.from_user.id
    state = get_data_for_user(uid)["state"]
    mode = get_data_for_user(uid)["mode"]

    if not check_user(callback):
        return

    if state != "Menu":
        bot.answer_callback_query(callback.id, "Сначала завершите текущую игру!", show_alert=True)
        return

    if mode == "City":
        start_game(callback, "City", "Arcade")
    elif mode == "Attractions":
        start_game(callback, "Attractions", "Arcade")


@bot.callback_query_handler(func=lambda c: c.data == "🏆 Рейтинг")
def rating(callback):
    uid = callback.from_user.id
    state = get_data_for_user(uid)["state"]

    if not check_user(callback):
        return

    if state != "Menu":
        bot.answer_callback_query(callback.id, "Сначала завершите текущую игру!", show_alert=True)
        return

    start_game(callback, "City", "Rating")

@bot.callback_query_handler(func=lambda c: c.data == "✈️ Экскурсионный")
def sightseeing_tour(callback):
    uid = callback.from_user.id
    state = get_data_for_user(uid)["state"]

    if not check_user(callback):
        return

    if state != "Menu":
        bot.answer_callback_query(callback.id, "Сначала завершите текущую игру!", show_alert=True)
        return

    start_game(callback, "Attractions", "Sightseeing_tour")

@bot.callback_query_handler(func=lambda c: c.data == "💼Следующий вопрос")
def next_question(callback):
    uid = callback.from_user.id
    data = get_data_for_user(uid)

    if not check_user(callback):
        return

    if data["state"] != "Game":
        bot.answer_callback_query(callback.id, "Сначала выберите режим в меню!", show_alert=True)
        return

    texts = {
        "City": "Укажите верный город!",
        "Gerb": "Укажите верный герб!",
        "Attractions": "Укажите верную достопримечательность!"
    }

    separation = {
        "City": 2,
        "Gerb": 2,
        "Attractions": 1
    }

    send_question(uid, texts[data["mode"]], separation[data["mode"]],  callback.id)

@bot.callback_query_handler(func=lambda c: c.data == "🛡 Гербы")
def gerbs(callback):
    uid = callback.from_user.id
    state = get_data_for_user(uid)["state"]

    update_row_value(uid, "mode", "Gerb")

    if not check_user(callback):
        return

    if state != "Menu":
        bot.answer_callback_query(callback.id, "Сначала завершите текущую игру!", show_alert=True)
        return

    start_game(callback, "Gerb")


@bot.callback_query_handler(func=lambda c: c.data == "🏛 Достопримечательности")
def attractions(callback):
    uid = callback.from_user.id
    state = get_data_for_user(uid)["state"]

    update_row_value(uid, "mode", "Attractions")

    if not check_user(callback):
        return
    if state != "Menu":
        bot.answer_callback_query(callback.id, "Сначала завершите текущую игру!", show_alert=True)
        return

    bot.edit_message_text(
        "Выберите режим:",
        callback.message.chat.id,
        callback.message.message_id,
        reply_markup=create_markup(["🎮 Аркадный", "✈️ Экскурсионный", "ℹ️ О режимах", "🚪 Выйти"], 1)
    )
    bot.answer_callback_query(callback.id)


@bot.callback_query_handler(func=lambda c: c.data == "🎲 Случайный режим")
def random_mode(callback):
    uid = callback.from_user.id
    state = get_data_for_user(uid)["state"]

    if not check_user(callback):
        return

    if state != "Menu":
        bot.answer_callback_query(callback.id, "Сначала завершите текущую игру!", show_alert=True)
        return

    mode, submode = random.choice(RANDOM_MODES)  # Выбирает случайный режим

    # Сохраняет режим в БД
    update_row_value(uid, "mode", mode)
    update_row_value(uid, "submode", submode)

    # Сообщение о том, какой режим выпал
    mode_names = {
        "City": "🏙 Города",
        "Gerb": "🛡 Гербы",
        "Attractions": "🏛 Достопримечательности"
    }

    # Для Городов показываем и подрежим
    if mode == "City":
        submode_names = {"Arcade": "Аркадный", "Rating": "Рейтинг"}
        bot.send_message(uid, f"🎲 Случайный режим! Выпал режим: {mode_names[mode]} — {submode_names.get(submode, submode)}")
    elif mode == "Attractions":
        submode_names = {"Arcade": "Аркадный", "Sightseeing_tour": "Экскурсионный"}
        bot.send_message(uid,
                         f"🎲 Случайный режим! Выпал режим: {mode_names[mode]} — {submode_names.get(submode, submode)}")
    else:
        bot.send_message(uid, f"🎲 Случайный режим! Выпал режим: {mode_names.get(mode, mode)}")

    # Запускает игру
    start_game(callback, mode, submode)

@bot.callback_query_handler(func=lambda c: c.data in ["🏁 Завершить", "🚪 Выйти"])
def finish(callback):
    uid = callback.from_user.id

    if not check_user(callback):
        return

    data = get_data_for_user(uid)
    mode, submode, glasses, most_points, score, right_answer = (
        data["mode"], data["submode"], data["glasses"], data["most_points"],
        data["score"], data["right_answer"]
    )

    # Режим Рейтинг — показывает итог, даже если пользователь сам выходит
    if mode == "City" and submode == "Rating":
        # Обновляет максимальные очки
        if glasses > most_points:
            update_row_value(uid, "most_points", glasses)

        bot.send_message(
            uid,
            f"Игра окончена!\nВерный ответ: {data['right_answer']}\nОчки: {data['glasses']}\n",
            reply_markup=create_markup(["🚪 Выйти"])
        )
        bot.answer_callback_query(callback.id)
        reset_table_value(uid)
        return

    # Сброс данных пользователя для следующей игры
    reset_table_value(uid)
    start(callback)
    bot.answer_callback_query(callback.id)


@bot.callback_query_handler(func=lambda c: c.data == "💡 Подсказка")
def hint(callback):
    uid = callback.from_user.id

    if not check_user(callback):
        return

    data = get_data_for_user(uid)
    if not data["hint"]:
        return

    if data["submode"] == "Rating" and data["glasses"] >= 6:
        update_row_value(uid, "glasses", data["glasses"] - 6)

    bot.send_photo(uid, data["hint"])
    bot.answer_callback_query(callback.id)

# -------------------- ОТВЕТЫ --------------------

@bot.callback_query_handler(func=lambda c: c.data not in SYSTEM_BUTTONS)
def answers(callback):
    uid = callback.from_user.id
    state = get_data_for_user(uid)["state"]
    if not check_user(callback):
        return

    if state != "Game":
        bot.answer_callback_query(callback.id, "Сначала выберите режим в меню!", show_alert=True)
        return

    data = get_data_for_user(uid)

    if callback.data == data["right_answer"]:
        update_row_value(uid, "score", data["score"] + 1)

        if data["mode"] == "City" and data["submode"] == "Rating":
            update_row_value(uid, "glasses", data["glasses"] + 10)

        if data["mode"] == "Attractions" and data["submode"] == "Sightseeing_tour":

            bot.send_message(
                uid,
                f'{data["documentation"]}',
                reply_markup=create_markup(["💼Следующий вопрос", "🚪 Выйти"], 1))
            bot.answer_callback_query(callback.id)
            return

        texts = {
            "City": "Укажите верный город!",
            "Gerb": "Укажите верный герб!",
            "Attractions": "Укажите верную достопримечательность!"
        }

        separation = {
            "City": 2,
            "Gerb": 2,
            "Attractions": 1
        }
        send_question(uid, texts[data["mode"]], separation[data["mode"]],  callback.id)

    else:
        if data["mode"] == "City" and data["submode"] == "Rating":
            # Обновляем максимальные очки, если текущие больше
            if data["glasses"] > data.get("most_points", 0):
                update_row_value(uid, "most_points", data["glasses"])

            finish(callback)
            bot.answer_callback_query(callback.id)
            return
        else:
            bot.send_message(uid, "❌ Неверно. Попробуйте ещё раз.")
            bot.answer_callback_query(callback.id)


# -------------------- POLLING --------------------

while True:
    try:
        bot.polling(non_stop=True, timeout=20)
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:
        logging.exception(e)
        time.sleep(5)