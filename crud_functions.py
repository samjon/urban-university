import sqlite3

# Функция для инициализации базы данных и создания таблиц
def initiate_db():
    conn = sqlite3.connect('products.db')  # Подключаемся к базе данных (или создаем её)
    cursor = conn.cursor()

    # Создаем таблицу Users, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    conn.commit()
    conn.close()

def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))

    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    exists = cursor.fetchone()[0] > 0

    conn.close()
    return exists


# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


def add_sample_products():
    products = [
        ("Product1", "Описание 1", 100),
        ("Product2", "Описание 2", 200),
        ("Product3", "Описание 3", 300),
        ("Product4", "Описание 4", 400)
    ]

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    for title, description, price in products:
        # Проверяем, существует ли продукт с таким названием
        cursor.execute('SELECT COUNT(*) FROM Products WHERE title = ?', (title,))
        exists = cursor.fetchone()[0] > 0

        if not exists:
            # Если продукт не существует, добавляем его
            cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (title, description, price))

    conn.commit()
    conn.close()

