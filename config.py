import random
from photo import *

BOT_TOKEN = ""

user_data = {}
user_collection = {}

DB_DIR = 'db'
DB_NAME = 'user database.db'
DB_TABLE_USERS_NAME = 'users'

# Передает основные изображения
def main_images(normalization):
    if normalization == "Greeting":
        with open("Photo/Greeting.png", "rb") as f:
            return f.read()
    elif normalization == "Transition_picture":
        with open("Photo/Transition_picture.png", "rb") as f:
            return f.read()
    return None

# Передает изображение и кнопки
def uploading_photos_buttons(received_elements, mode):
    if mode != "CityRating":
        available_cities = [
            name for name in cities.keys()
            if name not in received_elements
        ] # Создает список, учитывая ограничение
    else:
        available_cities = list(cities.keys()) # НЕ учитывает ограничение

    if not available_cities: # Выходит из функции, когда закончились уникальные города
        return None

    correct_city_name = random.choice(available_cities) # Выбирает один случайный элемент из списка
    city = cities[correct_city_name] # Принимает весь объект

    other_cities = [name for name in cities if name != correct_city_name] # Создает список из оставшихся городов
    wrong_cities = random.sample(other_cities, 3) # Выбирает три случайных неправильных элементов в виде списка

    options = wrong_cities + [correct_city_name] # Добавляется правильный элемент
    random.shuffle(options) # Перемешивает

    with open(city.photo_path, "rb") as f: # Читает файл
        photo_bytes = f.read()

    with open(city.map_path, "rb") as f: # Читает файл
        map_bytes = f.read()

    return photo_bytes, map_bytes, options, correct_city_name

