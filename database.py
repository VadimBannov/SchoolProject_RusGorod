import sqlite3
import logging
from config import *


# Функция для подключения к базе данных или создания новой, если её ещё нет
def create_db(database_name=DB_NAME):
    db_path = f'{database_name}'
    connection = sqlite3.connect(db_path)
    connection.close()

def execute_query(sql_query, data=None, db_path=None):
    if db_path is None:
        db_path = DB_NAME

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    if data:
        cursor.execute(sql_query, data)
    else:
        cursor.execute(sql_query)

    connection.commit()
    connection.close()

# Функция для выполнения любого sql-запроса для получения данных (возвращает значение)
def execute_selection_query(sql_query, data=None, db_path=f'{DB_NAME}'):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    if data:
        cursor.execute(sql_query, data)
    else:
        cursor.execute(sql_query)
    rows = cursor.fetchall()
    connection.close()
    return rows

# Функция для создания новой таблицы (если такой ещё нет)
# Получает название и список колонок в формате ИМЯ: ТИП
# Создаёт запрос CREATE TABLE IF NOT EXISTS имя_таблицы (колонка1 ТИП, колонка2 ТИП)
def create_table(table_name):
    sql_query = f'CREATE TABLE IF NOT EXISTS {table_name} ' \
                f'(id INTEGER PRIMARY KEY, ' \
                f'user_id INTEGER, ' \
                f'user_name TEXT, ' \
                f'state TEXT DEFAULT Menu,' \
                f'score INTEGER DEFAULT 1, ' \
                f'gauge TEXT DEFAULT None, ' \
                f'most_points INTEGER DEFAULT 0,' \
                f'mode TEXT DEFAULT None, ' \
                f'submode TEXT DEFAULT None, ' \
                f'cities_held TEXT DEFAULT None, ' \
                f'hint TEXT DEFAULT None, ' \
                f'right_answer TEXT DEFAULT None, ' \
                f'documentation TEXT DEFAULT None, ' \
                f'glasses INTEGER DEFAULT 0, ' \
                f'service_error INTEGER DEFAULT 0)'
    execute_query(sql_query)

# Функция для вывода всей таблицы (для проверки)
# Создаёт запрос SELECT * FROM имя_таблицы
def get_all_rows(table_name):
    sql_query = f"SELECT * FROM {table_name}"
    rows = execute_selection_query(sql_query)

    users = {}
    for row in rows:
        users[row[2]] = {
            "id": row[0],
            "user_id": row[1],
            "user_name": row[2],
            "state": row[3],
            "score": row[4],
            "gauge": row[5],
            "most_points": row[6],
            "mode": row[7],
            "submode": row[8],
            "cities_held": row[9],
            "hint": row[10],
            "right_answer": row[11],
            "documentation": row[12],
            "glasses": row[13],
            "service_error": row[14]
        }

    return users

# Функция для выведения таблицы лидеров
def get_most_points():
    sql = f"""
    SELECT user_name, most_points
    FROM {DB_TABLE_USERS_NAME}
    WHERE most_points > 0
    ORDER BY most_points DESC
    LIMIT 5
    """
    return execute_selection_query(sql)

# Функция для удаления всех записей из таблицы
# Создаёт запрос DELETE FROM имя_таблицы
def clean_table(table_name):
    execute_query(f"DELETE FROM {table_name}")

# Функция для вставки новой строки в таблицу
# Принимает список значений для каждой колонки и названия колонок
# Создаёт запрос INSERT INTO имя_таблицы (колонка1, колонка2) VALUES (?, ?)[значение1, значение2]
def initial_insertion(values):
    columns = "(user_id, user_name)"
    sq1_query = f"INSERT INTO {DB_TABLE_USERS_NAME} {columns} VALUES (?, ?)"
    execute_query(sq1_query, values)

# Функция для проверки, есть ли элемент в указанном столбце таблицы
# Создаёт запрос SELECT колонка FROM имя_таблицы WHERE колонка == значение LIMIT 1
def is_value_in_table(table_name, column_name, value):
    sq1_query = f"SELECT {column_name} FROM {table_name} WHERE {column_name} = ?"
    row = execute_selection_query(sq1_query, [value])
    return row

# Удалить пользователя по id
def delete_user(user_id):
    if is_value_in_table(DB_TABLE_USERS_NAME, "user_id", user_id):
        sq1_query = f"DELETE FROM {DB_TABLE_USERS_NAME} WHERE user_id = ?"
        execute_query(sq1_query, [user_id])

# Обновить значение в указанной строке и колонки
def update_row_value(user_id, column_name, new_value):
    if is_value_in_table(DB_TABLE_USERS_NAME, "user_id", user_id):
        sql_query = f"UPDATE {DB_TABLE_USERS_NAME} SET {column_name} = ? WHERE user_id = ?"
        execute_query(sql_query, [new_value, user_id])
    else:
        logging.info(f"DATABASE: Пользователь с id = {user_id} не найден")

# Функция для получения данных для указанного пользователя
def get_data_for_user(user_id):
    if is_value_in_table(DB_TABLE_USERS_NAME, "user_id", user_id):
        sq1_query = (f"SELECT user_id, user_name, state, score, gauge, most_points, mode, submode, cities_held, hint, right_answer, documentation, "
                     f"glasses, service_error FROM {DB_TABLE_USERS_NAME} "
                     f"WHERE user_id = ? limit 1")
        row = execute_selection_query(sq1_query, [user_id])[0]
        return {"user_id": row[0], "user_name": row[1], "state": row[2], "score": row[3], "gauge": row[4], "most_points": row[5], "mode": row[6], "submode": row[7], "cities_held": row[8],
                "hint": row[9], "right_answer": row[10], "documentation": row[11], "glasses": row[12], "service_error": row[13]}
    else:
        logging.info(f"DATABASE: Пользователь с id = {user_id} не найден")
        return {"user_id": "", "user_name": "", "state": "", "score": "", "gauge": "", "most_points": "", "mode": "", "submode": "", "cities_held": "", "hint": "",
                "right_answer": "", "documentation": "", "glasses": "",
                "service_error": ""}

# Функция обнуляет значение для указанного пользователя
def reset_table_value(user_id):
    if is_value_in_table(DB_TABLE_USERS_NAME, "user_id", user_id):
        sql_query = (
            f"UPDATE {DB_TABLE_USERS_NAME} "
            f"SET state = 'Menu', score = 1, gauge = NULL, mode = NULL, submode = NULL, cities_held = NULL, hint = NULL, right_answer = NULL, documentation = NULL, "
            f"glasses = 0 WHERE user_id = ?"
        )
        execute_query(sql_query, [user_id])
    else:
        logging.info(f"DATABASE: Пользователь с id = {user_id} не найден")



# Функция для подготовки базы данных
# Создаёт/подключается к бд, добавляет все таблицы, заполняет таблицу с промтами
def prepare_db(clean_if_exists=False):
    create_db()
    create_table(DB_TABLE_USERS_NAME)
    if clean_if_exists:
        clean_table(DB_TABLE_USERS_NAME)
