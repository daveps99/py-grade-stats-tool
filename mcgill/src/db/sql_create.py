import sqlite3
from sqlite3 import Error
from mcgill.src.db.sql_connect import Connection

class Creation():

    def __init__(self) -> None:
        self.connection = Connection().create_connection("students.db")

    def create_student_table(self):
        c = self.connection.cursor()
        try:
            c.execute("""CREATE TABLE students (
                        name text,
                        age integer,
                        grade integer,
                        major text
            )""")
            self.connection.commit()
        except:
            return "Table already created."

    def insert_student(self, student):
        c = self.connection.cursor()
        try:
            c.execute("INSERT INTO students VALUES ('{}', '{}', '{}', '{}')".format(
                student.get_name(),
                student.get_age(),
                student.get_grade(),
                student.get_major())
                )
            self.connection.commit()
        except Error as e:
            return "Student registration failed"

    def get_students_by_name(self, name):
        c = self.connection.cursor()
        try:
            c.execute("SELECT * FROM students WHERE name='{}'".format(name))
            print(c.fetchall())
            self.connection.commit()
        except Error as e:
            return "Student retrieval failed"

        


