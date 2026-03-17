

import sqlite3

# connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# create table
cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER)")

while True:
    print("1 Add Student")
    print("2 Show Students")
    print("3 Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")

        cursor.execute("INSERT INTO students VALUES (?,?)",(name,age))
        conn.commit()

    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)

    elif choice == "3":
        break