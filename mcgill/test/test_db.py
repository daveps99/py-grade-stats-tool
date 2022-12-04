import random
from mcgill.src.db.sql_create import Creation
from mcgill.src.db.sql_connect import Connection
from mcgill.src.student import Student
import unittest

class DBTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.creation = Creation()
        self.connection = Connection()

    def test_insert_student(self):
        mockId = random.randint(100000000,999999999)
        mockStudent = Student("David", 22, 85, "Software Engineering", mockId)
        
        self.creation.create_student_table()
        result = self.creation.insert_student(mockStudent)
        
        self.assertNotEqual(result, "Student registration failed")

        self.creation.remove_student(mockId)

    def test_get_students_by_name(self):
        mockId = random.randint(100000000,999999999)
        mockStudent = Student("Kyle", 22, 85, "Software Engineering", mockId)
        name = mockStudent.get_name()

        self.creation.create_student_table()
        self.creation.insert_student(mockStudent)

        result = self.creation.get_students_by_name(name)
        
        self.assertNotEqual(result, "Student retrieval failed")
        self.assertTrue(("Kyle",22,85,"Software Engineering", mockId) in result)

        self.creation.remove_student(mockId)

    def test_remove_student(self):
        mockId = random.randint(100000000,999999999)
        mockStudent = Student("REMOVE_TEST", 22, 85, "Software Engineering", mockId)

        self.creation.create_student_table()
        self.creation.insert_student(mockStudent)

        self.creation.remove_student(mockId)

        result = self.creation.get_students_by_name(mockStudent.get_name())

        self.assertEqual(result, [])



