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
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="log_file.txt", filemode="a",
)

# Функция для создания кнопок
def create_markup(labels, row_width=1):
    markup = InlineKeyboardMarkup(row_width=row_width)
    markup.add(*(InlineKeyboardButton(text=l, callback_data=l) for l in labels))
    return markup

def is_correct_answer(answer, user_id):
    return get_data_for_user(user_id)["right_answer"] == answer

# Безопасно распарсит JSON-строку в список. Возвращает [] при пустом/некорректном входе.
def safe_load_list(s):
    if not s:
        return []
    if isinstance(s, list):
        return s
    try:
        return json.loads(s)
    except (json.JSONDecodeError, TypeError, ValueError):
        return []


def check_application_PB(user_id):
    data = get_data_for_user(user_id)
    mode = data["mode"]
    held_raw = data["cities_held"]
    submode = data["submode"]

    held = safe_load_list(held_raw)

    result = uploading_photos_buttons(held, mode, submode)

    if result is None:
        update_row_value(user_id, "right_answer", None)
        return None

    photo, hint, options, correct = result

    held.append(correct)
    update_row_value(user_id, "cities_held", json.dumps(held, ensure_ascii=False))
    update_row_value(user_id, "right_answer", correct)
    update_row_value(user_id, "hint", hint)

    return photo, options

# Делает счёт
def update_score(user_id, delta=0):
    score = get_data_for_user(user_id)["score"] + delta
    update_row_value(user_id, "score", score)
    return score

def checking_for_user(callback_data):
    uid, uname = callback_data.from_user.id, callback_data.from_user.first_name
    if not is_value_in_table(DB_TABLE_USERS_NAME, "user_id", uid):
        initial_insertion([uid, uname])
        bot.send_message(
            uid,
            f"Техническая перезагрузка. Вы вернулись в главное меню."
        )
        main_menu(callback_data)
        return None
    return True



# Сообщения
# Возвращение на главное меню
@bot.callback_query_handler(func=lambda c: c.data == "🏁 Завершить")
@bot.callback_query_handler(func=lambda c: c.data == '🚪 Выйти')
def finish(callback):
    user_id = callback.from_user.id
    bot.answer_callback_query(callback.id)

    if checking_for_user(callback) is None:
        return

    data = get_data_for_user(user_id)
    mode, rating_finished, most_points, glasses, score, right_answer = (data["mode"], data["rating_finished"],
                                                                        data["most_points"], data["glasses"],
                                                                        data["score"], data["right_answer"])

    if mode == "City" and data["submode"] == "Rating":
        if glasses > most_points:
            update_row_value(user_id, "most_points", glasses)
        if rating_finished == 0:
            bot.send_message(
                user_id,
                f"Вы вышли из режима Рейтинг!\n"
                f"Верный город: {right_answer}\nПройденные уровни: {score}\nБаллы: {glasses}"
            )

    reset_table_value(user_id)

    main_menu(callback)



# Показывает подсказки
@bot.callback_query_handler(func=lambda c: c.data == "💡 Подсказка")
def hint_callback(callback):
    bot.answer_callback_query(callback.id)
    data = get_data_for_user(callback.from_user.id)

    if checking_for_user(callback) is None:
        return

    if data["mode"] == "City" and data["submode"] == "Rating" and data["glasses"] >= 6:
        update_row_value(callback.from_user.id, "glasses", data["glasses"] - 6)

    bot.send_photo(callback.from_user.id, data["hint"])


# Уведомление
@bot.message_handler(commands=["start"])
def start(message):
    uid, uname = message.from_user.id, message.from_user.first_name

    if not is_value_in_table(DB_TABLE_USERS_NAME, "user_id", uid):
        initial_insertion([uid, uname])

    bot.send_message(
        uid,
        "Всем здравствуйте! Это сообщение уведомляет о том, что данный проект находится в стадии разработки, и "
        "могут быть критические ошибки. Убедительная просьба указывать обо всех недочетах: лингвистических, "
        "технических... в личных сообщениях @molchalin68",
        reply_markup=create_markup(["Продолжить!"])
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    uid = message.from_user.id

    bot.send_message(
        uid,
        text="Проект в разработке. Сообщайте об ошибках @molchalin68"
    )

@bot.callback_query_handler(func=lambda c: c.data == '⭐ Список лидеров')
def leader(callback):
    uid = callback.from_user.id
    top = get_most_points()

    lines = []
    for i, (name, points) in enumerate(top, start=1):
        lines.append(f"{i}. {name} — {points}.")

    table = "\n".join(lines)

    bot.send_message(
        uid,
        text=f"Таблица лидеров:\n\n{table}"
    )

# debug и история запросов
@bot.message_handler(commands=['debug'])
def debug_command(message):
    with open("log_file.txt", "r", encoding="latin1") as f:
        bot.send_document(message.chat.id, f)



# Главное меню
@bot.callback_query_handler(func=lambda c: c.data == "Продолжить!")
def main_menu(callback):
    bot.send_message(
        callback.from_user.id,
        text="🇷🇺 РусГород\n Выберите режим:",
        reply_markup=create_markup(
            [
                "🏙 Города",
                "🛡 Гербы",
                "🏛 Достопримечательности",
                "🎲 Случайный режим",
                "⭐ Список лидеров",
                "ℹ️ О проекте"
            ]
        )
    )

# Режим "Город"
@bot.callback_query_handler(func=lambda c: c.data == "🏙 Города")
def city_modes(callback):
    update_row_value(callback.from_user.id, "mode", "City")

    if checking_for_user(callback) is None:
        return

    bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        text="Выберите режим:",
        reply_markup=create_markup(["🎮 Аркадный", "🏆 Рейтинг", "🚪 Выйти"])
    )


@bot.callback_query_handler(func=lambda c: c.data == '🛡 Гербы')
def gerb_modes(callback):
    user_id = callback.from_user.id
    update_row_value(callback.from_user.id, "mode", "Gerb")

    if checking_for_user(callback) is None:
        return

    result = check_application_PB(user_id)
    if not result:
        return

    photo, options = result
    options.extend(["🏁 Завершить"])

    bot.send_photo(
        user_id,
        photo,
        f"{get_data_for_user(user_id)['score']}. Что это за герб?",
        reply_markup=create_markup(options, row_width=2)
    )

@bot.callback_query_handler(func=lambda c: c.data == '🏛 Достопримечательности')
@bot.callback_query_handler(func=lambda c: c.data == '🎲 Случайный режим')
def process_callback_button2(callback_query):
    user_id = callback_query.from_user.id
    bot.answer_callback_query(callback_query.id)

    bot.send_message(user_id, "В разработке!")
    return

@bot.callback_query_handler(func=lambda c: c.data == 'ℹ️ О проекте')
def process_callback_button3(callback_query):
    user_id = callback_query.from_user.id
    bot.answer_callback_query(callback_query.id)

    bot.send_message(user_id, "Документация пишется!")
    return



def start_city_game(callback, submode):
    user_id = callback.from_user.id
    update_row_value(user_id, "submode", submode)

    if checking_for_user(callback) is None:
        return

    result = check_application_PB(user_id)
    if not result:
        return

    photo, options = result
    options.extend(["💡 Подсказка", "🏁 Завершить"])

    bot.send_photo(
        user_id,
        photo,
        f"{get_data_for_user(user_id)['score']}. Что это за город?",
        reply_markup=create_markup(options, row_width=2)
    )

@bot.callback_query_handler(func=lambda c: c.data == "🎮 Аркадный")
def king(callback):
    start_city_game(callback, "Arcade")

    if checking_for_user(callback) is None:
        return


@bot.callback_query_handler(func=lambda c: c.data == "🏆 Рейтинг")
def rating(callback):
    start_city_game(callback, "Rating")

    if checking_for_user(callback) is None:
        return


@bot.callback_query_handler()
def answers(callback):
    user_id = callback.from_user.id
    data = get_data_for_user(user_id)
    mode, score, glasses, right_answer, submode = (data["mode"], data["score"], data["glasses"], data["right_answer"],
                                                   data["submode"])

    if checking_for_user(callback) is None:
        return

    # Проверяет правильность ответа на текущий город
    if is_correct_answer(callback.data, user_id):

        # показывает новый город
        result = check_application_PB(user_id)
        if result is None: # Города закончились
            if mode == "City" and submode == "Arcade":
                bot.send_message(
                    user_id,
                    text="Все города пройдены.",
                    reply_markup=create_markup(["🚪 Выйти"])
                )
                return
            if mode == "Gerb":
                bot.send_message(
                    user_id,
                    text="Все гербы пройдены.",
                    reply_markup=create_markup(["🚪 Выйти"])
                )
                return

        photo, options = result

        # Добавляет стандартные кнопки
        if (mode == "City" and submode == "Arcade") or (mode == "City" and submode == "Rating"):
            options += ["💡 Подсказка", "🏁 Завершить"]
        else:
            options += ["🏁 Завершить"]

        if mode == "City" and submode == "Rating": # Начисляет очки только для Рейтинга
            update_row_value(user_id, "glasses", data["glasses"] + 10)
        score += 1
        update_row_value(user_id, "score", score) # Увеличивает счёт

        if mode == "City":
            bot.send_photo(
                user_id,
                photo,
                caption=f"✅ Верно!\n{score}. Что это за город?",
                reply_markup=create_markup(options, row_width=2)
            )
        if mode == "Gerb":
            bot.send_photo(
                user_id,
                photo,
                caption=f"✅ Верно!\n{score}. Что это за герб?",
                reply_markup=create_markup(options, row_width=2)
            )

    else:
        # Неверный ответ
        if mode == "City" and submode == "Rating":
            update_row_value(user_id, "rating_finished", 1)
            update_row_value(user_id, "most_points", glasses)
            bot.send_message(
                user_id,
                f"Игра закончена!\n"
                f"Верный город: {right_answer}\nПройденные уровни: {score}\nБаллы: {glasses}",
                reply_markup=create_markup(["🚪 Выйти"])
            )
        else:
            if right_answer is not None:
                bot.send_message(
                    user_id,
                    "Неверно! Попробуйте ещё раз."
            )


while True:
    try:
        bot.polling(non_stop=True, interval=0, timeout=20)

    except requests.exceptions.ConnectionError:
        execute_query(
            f"UPDATE {DB_TABLE_USERS_NAME} SET service_error = 1"
        )
        time.sleep(5)

    except Exception as e:
        logging.exception(e)
        time.sleep(5)