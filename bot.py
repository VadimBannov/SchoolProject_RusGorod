import telebot
import json
import time
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
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
    data = get_data_for_user(user_id)
    if data and data.get("service_error") == 1:
        bot.send_message(
            user_id,
            "⚠️ Соединение с сервером временно пропадало. Игра продолжена."
        )
        update_row_value(user_id, "service_error", 0)

    held = safe_load_list(held_raw)

    result = uploading_photos_buttons(held, mode)
    if result is None:
        update_row_value(user_id, "right_answer", "end")
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



# Сообщения
# Возвращение на главное меню
@bot.callback_query_handler(func=lambda c: c.data == "Завершить➡️")
def finish(callback):
    user_id = callback.from_user.id
    bot.answer_callback_query(callback.id)

    data = get_data_for_user(user_id)
    mode, rating_finished, most_points, glasses, score = (data["mode"], data["rating_finished"], data["most_points"],
                                                          data["glasses"], data["score"])

    if mode == "CityRating":
        if glasses > most_points:
            update_row_value(user_id, "most_points", glasses)
        if rating_finished == 0:
            bot.send_message(
                user_id,
                f"Вы вышли из режима Рейтинг.\nСчёт: {score}, Баллы: {glasses}"
            )

    reset_table_value(user_id)

    main_menu(callback)



# Показывает подсказки
@bot.callback_query_handler(func=lambda c: c.data == "Подсказка⏰")
def hint_callback(callback):
    bot.answer_callback_query(callback.id)
    data = get_data_for_user(callback.from_user.id)

    if data["mode"] == "CityRating" and data["glasses"] >= 5:
        update_row_value(callback.from_user.id, "glasses", data["glasses"] - 5)

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

@bot.message_handler(commands=["leader"])
def leader(message):
    uid = message.from_user.id
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
    bot.send_photo(
        callback.from_user.id,
        main_images("Greeting"),
        caption="«РусГород» — викторина по городам, флагов городов и достопримечательностей России. Вам будет "
                "предоставлена картинка с определённом объектом, и вместе с нею будут предложены варианты ответов. "
                "Данный проект намерен познакомить вас с уникальными территориально-культурными ценностями народов "
                "России🇷🇷🇺 \n\nВыберите категорию:",
        reply_markup=create_markup(
            [
                "⏔⏔⏔ Города ⏔⏔⏔",
                "⏔⏔⏔ Гербы городов ⏔⏔⏔",
                "⏔⏔⏔ Достопримечательности ⏔⏔⏔"
            ]
        )
    )

# Режим "Город"
@bot.callback_query_handler(func=lambda c: c.data == "⏔⏔⏔ Города ⏔⏔⏔")
def city_modes(callback):
    update_row_value(callback.from_user.id, "mode", "City")

    bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            main_images("Transition_picture"),
            caption="Царь горы — это аркадный режим, где нет ограничений на попытки и города не повторяются.\n"
                    "Рейтинг — бесконечный режим с одной попыткой, результаты которой попадают в таблицу лидеров (/leader).\n\n"
                    "Выберите режим:"),
        reply_markup=create_markup(["Царь горы", "Рейтинг", "Завершить➡️"])
    )


@bot.callback_query_handler(func=lambda c: c.data == '⏔⏔⏔ Гербы городов ⏔⏔⏔')
@bot.callback_query_handler(func=lambda c: c.data == '⏔⏔⏔ Достопримечательности ⏔⏔⏔')
def process_callback_button2(callback_query):
    user_id = callback_query.from_user.id
    bot.answer_callback_query(callback_query.id)

    bot.send_message(user_id, "В разработке!")
    return

def start_city_game(callback, mode):
    user_id = callback.from_user.id
    update_row_value(user_id, "mode", mode)

    result = check_application_PB(user_id)
    if not result:
        return

    photo, options = result
    options.extend(["Подсказка⏰", "Завершить➡️"])

    bot.send_photo(
        user_id,
        photo,
        f"{get_data_for_user(user_id)['score']}. Что это за город?",
        reply_markup=create_markup(options, row_width=2)
    )

@bot.callback_query_handler(func=lambda c: c.data == "Царь горы")
def king(callback):
    start_city_game(callback, "CityKing")


@bot.callback_query_handler(func=lambda c: c.data == "Рейтинг")
def rating(callback):
    start_city_game(callback, "CityRating")


@bot.callback_query_handler()
def answers(callback):
    user_id = callback.from_user.id
    data = get_data_for_user(user_id)
    mode, score, glasses = data["mode"], data["score"], data["glasses"]

    # Проверяет правильность ответа на текущий город
    if is_correct_answer(callback.data, user_id):
        if mode == "CityRating": # Начисляет очки только для Рейтинга
            update_row_value(user_id, "glasses", data["glasses"] + 10)
        score += 1
        update_row_value(user_id, "score", score) # Увеличивает счёт

        # показывает новый город
        result = check_application_PB(user_id)
        if result is None: # Города закончились
            if mode == "CityKing":
                bot.send_message(user_id, "Все города пройдены. Вы автоматически вышли.")
                finish(callback)
            else:
                bot.send_message(
                    user_id,
                    f"Игра закончена!\nСчёт: {data['score']}, Баллы: {data['glasses']}",
                    reply_markup=create_markup(["Завершить➡️"])
                )
            return

        photo, options = result
        # Добавляет стандартные кнопки
        if mode == "CityRating" or mode == "CityKing":
            options += ["Подсказка⏰", "Завершить➡️"]

        bot.send_photo(
            user_id,
            photo,
            caption=f"{score}. Что это за город?",
            reply_markup=create_markup(options, row_width=2)
        )

    else:
        # Неверный ответ
        if mode == "CityRating":
            update_row_value(user_id, "rating_finished", 1)
            update_row_value(user_id, "most_points", glasses)
            bot.send_message(
                user_id,
                f"Неверно! В Рейтинге доступна только одна попытка.\n"
                f"Счёт: {data['score']}, Баллы: {data['glasses']}",
                reply_markup=create_markup(["Завершить➡️"])
            )
        else:
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