from mcgill.src.db.sql_connect import Connection
from mcgill.src.db.sql_create import Creation

class Student():

    def __init__(self, name, age, grade, major) -> None:
        self.name = name
        self.age = age
        self.grade = grade
        self.major = major

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def get_major(self):
        return self.major

    def post_student(self):
        connection = Connection().create_connection("../../students.db")
        Creation().create_student_table(connection)
        Creation().insert_student(connection, self)

        

