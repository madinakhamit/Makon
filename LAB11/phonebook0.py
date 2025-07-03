import psycopg2
import csv
from tabulate import tabulate
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="Password123",
    port=5432
)

cur = conn.cursor()

# Функция для вывода уведомлений
def check_notifications():
    if conn.notices:
        for notice in conn.notices:
            print(f"PostgreSQL Notice: {notice}")
        conn.notices.clear()

        

# Создание таблицы, если она еще не существует
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL UNIQUE
)
""")

flag = True
names_list = ['Alice', 'Oleg']
surnames_list = ['Smith', 'Johnson']
phones_list = ['12345', '874564545']

while flag:
    print("""
    commands:
    "1"- to INSERT data to the table.
    "2"- to UPDATE data in the table.
    "3"- to make specific QUERY in the table.
    "4"- to DELETE data from the table.
    "5"- to see the values in the table.
    "6"- to see with limit
    "0"- to close the program.
    """)
    
    com = str(input())
    
    # Insert data
    if com == "1":
        print('1 - "csv"\n2 - to fill out info yourself write\n3 - with list of users')
        act = str(input())
        
        # csv
        if act == "1":
            filepath = input("Enter a file path with proper extension: ")

            with open(filepath, 'r') as f:
                reader = list(csv.reader(f))  # list в листе где элементы строки
                print("\nДанные из CSV файла:")
                for i in range(len(reader)-1):
                    print(f"{i+1}: {reader[i+1]}")

                row_num = int(input("Введите номер строки, которую хотите добавить: "))
                row = reader[row_num]

                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", 
                            (row[0], row[1], row[2]))
                conn.commit()

            input("\n\nНажмите Enter, чтобы вернуться в меню...")
        
        # Yourself
        if act == "2":
            name_var = str(input("Name: "))
            surname_var = str(input("Surname: "))
            phone_var = str(input("Phone: "))
            cur.execute("call insert_or_update_user(%s,%s,%s)",(name_var,surname_var,phone_var))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
        
        # Insert with list
        if act == '3':
            cur.execute("CALL insert_many_users(%s, %s, %s)", (names_list, surnames_list, phones_list))
            conn.commit()

            # Вывод уведомлений из базы данных
            check_notifications()
    # Update
    if com == '2':
        act = str(input('the name of the column that you want to change: '))
        if act == "name":
            name_var = str(input("Enter name that you want to change: "))
            name_upd = str(input("Enter the new name: "))
            cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (name_upd, name_var,))
            conn.commit()
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
        
        if act == "surname":
            surname_var = str(input("Enter surname that you want to change: "))
            surname_upd = str(input("Enter the new surname: "))
            cur.execute("UPDATE phonebook SET surname = %s WHERE surname = %s", (surname_upd, surname_var,))
            conn.commit()
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
        
        if act == "phone":
            phone_var = str(input("Enter phone number that you want to change: "))
            phone_upd = str(input("Enter the new phone number: "))
            cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (phone_upd, phone_var,))
            conn.commit()
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
    
    # Query
    if com == "3":
        act = str(input("choose column : \nid -- '1' \nname -- '2' \nsurname -- '3' \nphone -- '4' \n"))
        if act == "1":
            id_var = str(input("Type id of the user: "))
            cur.execute("SELECT * from query(%s,%s)", (act,id_var))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
        
        if act == "2":
            name = str(input("Type name of the user: "))
            cur.execute("SELECT * from query(%s,%s)", (act,name))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
        
        if act == "3":
            surname = str(input("Type surname of the user: "))
            cur.execute("SELECT * from query(%s,%s)", (act,surname))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
        
        if act == "4":
            phone = str(input("Type phone number of the user: "))
            cur.execute("SELECT * from query(%s,%s)", (act,phone))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
    
    # Delete
    if com == "4":
        type_com = str(input("'1'-delete on name and  '2'- delete on phone\n"))
        if type_com == "1":
            user_name = str(input('Type user_name which you want to delete: '))
            cur.execute("call del(%s,%s)", (type_com,user_name))
        elif type_com == "2":
            phone_var = str(input('Type phone which you want to delete: '))
            cur.execute("call del(%s,%s)", (type_com,phone_var))

        input("\n\nНажмите Enter, чтобы вернуться в меню...")    
    
    # Display
    if com == "5":
        cur.execute("SELECT * from phonebook;")
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
        input("\n\nНажмите Enter, чтобы вернуться в меню...")
    
    # Display with limit
    if com == "6":
        limit = int(input("limit of rows:"))
        offset = int(input("с какого начать:"))
        cur.execute("SELECT user_id, name, surname, phone from get_users(%s,%s);",(limit,offset))
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
        input("\n\nНажмите Enter, чтобы вернуться в меню...")

    # Finish
    if com == "0":
        flag = False

# Закрытие соединения
conn.commit()
cur.close()
conn.close()