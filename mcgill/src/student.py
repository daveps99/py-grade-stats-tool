from mcgill.src.db.sql_connect import Connection
from mcgill.src.db.sql_create import Creation
import random

class Student():

    def __init__(self, name, age, grade, major, id) -> None:
        self.name = name
        self.age = age
        self.grade = grade
        self.major = major
        self.id = id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def get_major(self):
        return self.major

    #This id is unique to each student
    def get_id(self):
        return self.id


