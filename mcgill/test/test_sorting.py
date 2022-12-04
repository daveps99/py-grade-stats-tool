import random
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
        mockIdA = random.randint(100000000,999999999)
        mockIdB = random.randint(100000000,999999999)
        mockIdC = random.randint(100000000,999999999)
        mockStudentA = Student("GRADE_SORT_TEST", 22, 10, "Software Engineering", mockIdA)
        mockStudentB = Student("GRADE_SORT_TEST", 22, 100, "Software Engineering", mockIdB)
        mockStudentC = Student("GRADE_SORT_TEST", 22, 50, "Software Engineering", mockIdC)
        
        name = mockStudentA.get_name()

        self.creation.insert_student(mockStudentA)
        self.creation.insert_student(mockStudentB)
        self.creation.insert_student(mockStudentC)

        result = self.sorting.sortStudentsByGrade(name)
        sorted_list = [("GRADE_SORT_TEST", 22, 10, "Software Engineering", mockIdA),("GRADE_SORT_TEST", 22, 50, "Software Engineering", mockIdC),("GRADE_SORT_TEST", 22, 100, "Software Engineering", mockIdB)]
        
        self.assertIsNotNone(result)
        self.assertEqual(result, sorted_list)

        self.creation.remove_student(mockIdA)
        self.creation.remove_student(mockIdB)
        self.creation.remove_student(mockIdC)

    def test_age_sort(self):
        mockIdA = random.randint(100000000,999999999)
        mockIdB = random.randint(100000000,999999999)
        mockIdC = random.randint(100000000,999999999)
        mockStudentA = Student("AGE_SORT_TEST", 20, 10, "Software Engineering", mockIdA)
        mockStudentB = Student("AGE_SORT_TEST", 10, 100, "Software Engineering", mockIdB)
        mockStudentC = Student("AGE_SORT_TEST", 30, 50, "Software Engineering", mockIdC)
        
        name = mockStudentA.get_name()

        self.creation.insert_student(mockStudentA)
        self.creation.insert_student(mockStudentB)
        self.creation.insert_student(mockStudentC)

        result = self.sorting.sortStudentsByAge(name)
        sorted_list = [("AGE_SORT_TEST", 10, 100, "Software Engineering", mockIdB),("AGE_SORT_TEST", 20, 10, "Software Engineering", mockIdA),("AGE_SORT_TEST", 30, 50, "Software Engineering", mockIdC)]

        self.assertIsNotNone(result)
        self.assertEqual(result, sorted_list)

        self.creation.remove_student(mockIdA)
        self.creation.remove_student(mockIdB)
        self.creation.remove_student(mockIdC)

    def test_major_sort(self):
        mockIdA = random.randint(100000000,999999999)
        mockIdB = random.randint(100000000,999999999)
        mockIdC = random.randint(100000000,999999999)
        mockStudentA = Student("MAJOR_SORT_TEST", 20, 10, "A", mockIdA)
        mockStudentB = Student("MAJOR_SORT_TEST", 10, 100, "D", mockIdB)
        mockStudentC = Student("MAJOR_SORT_TEST", 30, 50, "C", mockIdC)
        
        name = mockStudentA.get_name()

        self.creation.insert_student(mockStudentA)
        self.creation.insert_student(mockStudentB)
        self.creation.insert_student(mockStudentC)

        result = self.sorting.sortStudentsByMajor(name)
        sorted_list = [("MAJOR_SORT_TEST", 20, 10, "A", mockIdA),("MAJOR_SORT_TEST", 30, 50, "C", mockIdC),("MAJOR_SORT_TEST", 10, 100, "D", mockIdB)]

        self.assertIsNotNone(result)
        self.assertEqual(result, sorted_list)

        self.creation.remove_student(mockIdA)
        self.creation.remove_student(mockIdB)
        self.creation.remove_student(mockIdC)
