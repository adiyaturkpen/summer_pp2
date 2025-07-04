import psycopg2       # Для подключения и работы с PostgreSQL
import csv            # Для чтения данных из CSV-файла
from tabulate import tabulate  # Для красивого вывода таблиц в консоль

# === Функция для подключения к базе данных ===
def connect_db():
    return psycopg2.connect(
        host="localhost",         # Адрес сервера PostgreSQL
        database="phonebook",     # Название базы данных
        user="postgres",          # Имя пользователя
        password="21062007",      # Пароль к базе
        port=5432                 # Порт по умолчанию для PostgreSQL
    )

# === Добавление одной записи вручную ===
def insert_from_console(conn):
    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Телефон: ")

    with conn.cursor() as cur:  # Открываем курсор (объект для выполнения SQL-запросов)
        cur.execute(
            "INSERT INTO phonebook2 (name, surname, phone) VALUES (%s, %s, %s)",
            (name, surname, phone)
        )
        conn.commit()  # Сохраняем изменения в базе данных
        print("✔ Добавлено!")

# === Добавление записей из CSV-файла ===
def insert_from_csv(conn):
    path = input("Укажите путь к .csv: ")
    with open(path, newline='') as f:       # Открываем CSV-файл
        reader = csv.reader(f)              # Создаем читатель CSV
        next(reader)                        # Пропускаем первую строку (заголовок)
        with conn.cursor() as cur:
            for row in reader:
                if len(row) == 3:           # Проверяем, что строка содержит 3 поля
                    cur.execute(
                        "INSERT INTO phonebook2 (name, surname, phone) VALUES (%s, %s, %s)",
                        (row[0], row[1], row[2])
                    )
        conn.commit()
        print("✔ CSV загружен!")

# === Обновление данных в таблице ===
def update_entry(conn):
    column = input("Что изменить (name / surname / phone): ")  # Выбор столбца
    old_value = input("Что нужно заменить: ")
    new_value = input("На что заменить: ")

    with conn.cursor() as cur:
        # Формируем SQL-запрос с подстановкой названия столбца
        query = f"UPDATE phonebook2 SET {column} = %s WHERE {column} = %s"
        cur.execute(query, (new_value, old_value))
        conn.commit()
        print("✔ Обновлено!")

# === Поиск записей в таблице ===
def query(conn):
    column = input("По какому полю искать (id / name / surname / phone): ")
    value = input("Введите значение: ")

    with conn.cursor() as cur:
        query = f"SELECT * FROM phonebook2 WHERE {column} = %s"
        cur.execute(query, (value,))
        rows = cur.fetchall()  # Получаем все найденные строки

        # Выводим таблицу с заголовками и красивым оформлением
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

# === Удаление записи по номеру телефона ===
def delete_entry(conn):
    phone = input("Введите номер телефона для удаления: ")

    with conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook2 WHERE phone = %s", (phone,))
        conn.commit()
        print("✔ Удалено!")

# === Показ всех записей в таблице ===
def show_all(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook2")
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

# === Главная функция — меню программы ===
def main():
    conn = connect_db()  # Подключаемся к базе данных
    while True:
        print("""
======================
1 - Добавить вручную
2 - Загрузить CSV
3 - Обновить запись
4 - Найти запись
5 - Удалить запись
6 - Показать всё
7 - Выход
======================
        """)
        choice = input("Выбор: ")

        # Выполняем соответствующую функцию в зависимости от выбора пользователя
        if choice == "1":
            insert_from_console(conn)
        elif choice == "2":
            insert_from_csv(conn)
        elif choice == "3":
            update_entry(conn)
        elif choice == "4":
            query(conn)
        elif choice == "5":
            delete_entry(conn)
        elif choice == "6":
            show_all(conn)
        elif choice == "7":
            break  # Выход из программы
        else:
            print("❌ Неверный выбор.")

    conn.close()  # Закрываем соединение с базой

# === Точка входа в программу ===
if __name__ == "__main__":
    main()
