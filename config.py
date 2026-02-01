import random
from photo import *

BOT_TOKEN = ""

user_data = {}
user_collection = {}

DB_DIR = 'db'
DB_NAME = 'user database.db'
DB_TABLE_USERS_NAME = 'users'

SYSTEM_BUTTONS = {
    "🚪 Выйти",
    "🏁 Завершить",
    "💡 Подсказка",
    "⭐ Список лидеров",
    "ℹ️ О проекте",
    "Продолжить!",
    "🎮 Аркадный",
    "🏆 Рейтинг",
    "🏙 Города",
    "🛡 Гербы",
    "🏛 Достопримечательности",
    "🎲 Случайный режим",
}

DOCUMENTATION = (f"🇷🇺 РусГород — это познавательная игра, посвящённая городам России. \n\n"
                 f"В проекте вы можете:\n"
                 f"• 🏙 угадывать города по фотографиям\n"
                 f"• 🛡 распознавать гербы городов\n"
                 f"• 🏛 узнавать достопримечательности\n"
                 f"• 🎲 играть в случайном режиме\n"
                 f" • 🏆 соревноваться за место в таблице лидеров\n\n"
                 f"Игра построена в формате викторины: выбирайте правильный вариант, зарабатывайте очки и проверяйте свои знания географии и культуры России.\n\n"
                 f"Режимы:\n"
                 f"🎮 Аркадный — в этом режиме игра имеет завершение. В ходе прохождения игры вы сможете увидеть уникальный город, который в раунде не повторится. Количество попыток не ограничены, однако очки рейтинга не будут учитываться.\n"
                 f"🏆 Рейтинг — бесконечный режим. В этом режиме не предоставляется возможность совершить ошибки. За каждое успешное действие начисляются рейтинговые очки. Режим предназначен для соревнований между игроками.\n\n"
                 f"⭐️ Очки рейтинга вы можете зарабатывать в специальном режиме «🏆 Рейтинг», который предназначен исключительно для ГОРОДОВ (в список не входят флаги и достопримечательности)")

RANDOM_MODES = [
    ("City", "Arcade"),
    ("City", "Rating"),
    ("Gerb", None),
    ("Attractions", None),
]


# Передает изображение и кнопки
def uploading_photos_buttons(received_elements, actual_mode, submode):
    storage_mode = ""
    get_image = ""

    if actual_mode == "City": # Проверяет пользовательский режим
        storage_mode = cities
        get_image = lambda obj: obj.photo_path
    elif actual_mode == "Gerb":
        storage_mode = gerbs
        get_image = lambda obj: obj.photo_path
    elif actual_mode == "Attractions":
        storage_mode = attractions
        get_image = lambda obj: obj.photo_path

    if submode != "Rating": # Проверяет есть ли подрежим Рейтинг
        available = [
            name for name in storage_mode
            if name not in received_elements
        ]
    else:
        available = list(storage_mode.keys())

    if not available: # Выходит из функции, когда закончились уникальные города
        return None

    correct_name = random.choice(available) # Выбирает один случайный элемент из списка
    correct_obj = storage_mode[correct_name] # Принимает весь объект

    other_names = [name for name in storage_mode if name != correct_name] # Создает список из оставшихся объектов
    wrong_names = random.sample(other_names, min(3, len(other_names))) # Выбирает три случайных неправильных элементов в виде списка

    options = wrong_names + [correct_name] # Добавляется правильный элемент
    random.shuffle(options) # Перемешивает

    with open(get_image(correct_obj), "rb") as f: # Читает файлы
        image_bytes = f.read()

    if actual_mode == "City":
        with open(correct_obj.map_path, "rb") as f:
            map_bytes = f.read()
    else:
        map_bytes = None

    return image_bytes, map_bytes, options, correct_name



