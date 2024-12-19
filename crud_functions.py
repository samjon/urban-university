import sqlite3


# Функция для инициализации базы данных и создания таблицы Products
def initiate_db():
    conn = sqlite3.connect('products.db')  # Подключаемся к базе данных (или создаем её)
    cursor = conn.cursor()

    # Создаем таблицу Products, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


# Функция для добавления тестовых данных (можно использовать для первоначального заполнения)
def add_sample_products():
    products = [
        ("Omega-3", "fish oil", 100),
        ("Vitamin C", "Витамин С", 200),
        ("B-complex", "B-комплекс", 300),
        ("Hyaluronic acid", "Гиалуроновая кислота", 400)
    ]

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)

    conn.commit()
    conn.close()
