import psycopg2
import csv
from tabulate import tabulate

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="21062007",
        port=5432
    )

def insert_from_console(conn):
    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Телефон: ")

    with conn.cursor() as cur:
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                    (name, surname, phone))
        conn.commit()
        print("✔ Добавлено!")

def insert_from_csv(conn):
    path = input("Укажите путь к .csv: ")
    with open(path, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # пропускаем заголовок
        with conn.cursor() as cur:
            for row in reader:
                if len(row) == 3:
                    cur.execute("INSERT INTO phonebook2 (name, surname, phone) VALUES (%s, %s, %s)",
                                (row[0], row[1], row[2]))
        conn.commit()
        print("✔ CSV загружен!")

def update_entry(conn):
    column = input("Что изменить (name / surname / phone): ")
    old_value = input("Что нужно заменить: ")
    new_value = input("На что заменить: ")

    with conn.cursor() as cur:
        query = f"UPDATE phonebook SET {column} = %s WHERE {column} = %s"
        cur.execute(query, (new_value, old_value))
        conn.commit()
        print("✔ Обновлено!")

def query(conn):
    column = input("По какому полю искать (id / name / surname / phone): ")
    value = input("Введите значение: ")

    with conn.cursor() as cur:
        query = f"SELECT * FROM phonebook WHERE {column} = %s"
        cur.execute(query, (value,))
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def delete_entry(conn):
    phone = input("Введите номер телефона для удаления: ")

    with conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        conn.commit()
        print("✔ Удалено!")

def show_all(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook2")
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def main():
    conn = connect_db()
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
            break
        else:
            print("❌ Неверный выбор.")

    conn.close()

if __name__ == "__main__":
    main()
