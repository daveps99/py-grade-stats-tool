import sys
from mcgill.src.db.sql_create import Creation
from mcgill.src.db.sql_connect import Connection
from mcgill.src.student import Student
import unittest

class DBTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.creation = Creation()
        self.connection = Connection()

    def test_insert_student(self):
        mockStudent = Student("David", 22, 85, "Software Engineering")
        
        self.creation.create_student_table()

        result = self.creation.insert_student(mockStudent)
        print("Student inserted")

        self.assertNotEqual(result, "Student registration failed")

    def test_get_student_by_name(self):
        mockStudent = Student("Kyle", 22, 85, "Software Engineering")
        name = mockStudent.get_name()

        self.creation.insert_student(mockStudent)

        result = self.creation.get_students_by_name(name)

        self.assertNotEqual(result, "Student retrieval failed")



