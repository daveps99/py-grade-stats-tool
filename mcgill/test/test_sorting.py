import sys
from mcgill.src.db.sql_create import Creation
from mcgill.src.db.sql_connect import Connection
from mcgill.src.sorting import Sorting
from mcgill.src.student import Student
import unittest

class SortingTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.creation = Creation()
        self.connection = Connection()
        self.sorting = Sorting()

    def test_grade_sort(self):
        mockStudent = Student("Bob", 22, 70, "Software Engineering")
        
        name = mockStudent.get_name()

        self.creation.insert_student(mockStudent)

        result = self.sorting.sortStudentsByGrade(name)

        self.assertIsNotNone(result)

    def test_name_sort(self):
        mockStudent = Student("Bob", 22, 70, "Software Engineering")
        
        name = mockStudent.get_name()

        self.creation.insert_student(mockStudent)

        result = self.sorting.sortStudentsByName(name)

        self.assertIsNotNone(result)

    def test_age_sort(self):
        mockStudent = Student("Bob", 22, 70, "Software Engineering")
        
        name = mockStudent.get_name()

        self.creation.insert_student(mockStudent)

        result = self.sorting.sortStudentsByAge(name)

        self.assertIsNotNone(result)

    def test_major_sort(self):
        mockStudent = Student("Bob", 22, 70, "Software Engineering")
        
        name = mockStudent.get_name()

        self.creation.insert_student(mockStudent)

        result = self.sorting.sortStudentsByMajor(name)

        self.assertIsNotNone(result)
