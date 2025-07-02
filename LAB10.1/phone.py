import psycopg2
import csv
from tabulate import tabulate 


conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="Password123",
    port=5432,
    client_encoding="UTF8"

)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL

)
""")

flag = True



while flag:
    print("""
    commands:
    "1"- to INSERT data to the table.
    "2"- to UPDATE data in the table.
    "3"- to make specidific QUERY in the table.
    "4"- to DELETE data from the table.
    "5"- to see the values in the table.
    "0"- to close the program.      
    """)
    com = str(input())
    
    #insert
    if com == "1":
        print('if "csv" write -- 1 or if want to fill out info yoerslef write - 2')
        act = str(input())
        #csv
        if act == "1":
            filepath = input("Enter a file path with proper extension: ")
            with open(str(filepath), 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
            conn.commit()
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
        #yourself
        if act == "2":
            name_var = str(input("Name: "))
            surname_var = str(input("Surname: "))
            phone_var = str(input("Phone: "))
            cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name_var, surname_var, phone_var))
            conn.commit()
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
    #update
    if com == '2':
        act = str(input('the name of the column that you want to change: '))
        if act == "name":
            name_var = str(input("Enter name that you want to change: "))
            name_upd = str(input("Enter the new name: "))
            cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (name_upd, name_var))
            conn.commit()
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
       

        if act == "surname":
            surname_var = str(input("Enter surname that you want to change: "))
            surname_upd = str(input("Enter the new surname: "))
            cur.execute("UPDATE phonebook SET surname = %s WHERE surname = %s", (surname_upd, surname_var))
            conn.commit()
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
           
           
        if act == "phone":
            phone_var = str(input("Enter phone number that you want to change: "))
            phone_upd = str(input("Enter the new phone number: "))
            cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (phone_upd, name_var))
            conn.commit()
            input("\n\nНажмите Enter, чтобы вернуться в меню...")
      
      
                
    #query
    if com == "3":    
        act = str(input("choose column : \nid -- '1' \nname -- '2' \nsurname -- '3' \nphone -- '4' \n"))
        if act == "1":
            id_var = str(input("Type id of the user: "))
            cur.execute("SELECT * FROM phonebook WHERE user_id = %s", (id_var, ))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")

        
        if act == "2":
            name = str(input("Type name of the user: "))
            cur.execute("SELECT * FROM phonebook WHERE name = %s", (name, ))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")

        
        if act == "3":
            surname = str(input("Type surname of the user: "))
            cur.execute("SELECT * FROM phonebook WHERE surname = %s", (surname, ))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")

           
        if act == "4":
            phone = str(input("Type phone number of the user: "))
            cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone, ))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
            input("\n\nНажмите Enter, чтобы вернуться в меню...")

    #delete
    if com == "4":
        phone_var = str(input('Type phone number which you want to delete: '))
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone_var,))
        conn.commit()
        input("\n\nНажмите Enter, чтобы вернуться в меню...")    
    
    #display
    if com  == "5":
        cur.execute("SELECT * from phonebook;")
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
        input("\n\nНажмите Enter, чтобы вернуться в меню...")

      
    #finish
    if com == "0":
        flag = False
    

conn.commit()
cur.close()
conn.close()