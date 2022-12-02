import sys
from mcgill.src.db.sql_create import Creation
from mcgill.src.db.sql_connect import Connection
from mcgill.src.student import Student
from mcgill.src.statistics import Statistics
import unittest

class testStatistic(unittest.TestCase):
    
    def setUp(self) -> None:
        self.creation = Creation()
        self.connection = Connection()
        self.statistics = Statistics()


    def test_grade_mean(self):
        mockStudent1 = Student("Yacine", 22, 85, "Software Engineering")
        mockStudent2 = Student("Yacine" , 22, 72, "Software Engineering")
        mockStudent3 = Student("Yacine" , 22, 94, "Software Engineering")
        mockStudent4 = Student("Yacine" , 22, 57, "Software Engineering")

        mean = (85 + 72 + 94 +57)/4

        
        self.creation.create_student_table()


        
        result1 = self.creation.insert_student(mockStudent1)
        result2 = self.creation.insert_student(mockStudent2)
        result3 = self.creation.insert_student(mockStudent3)
        result4 = self.creation.insert_student(mockStudent4)


        #check that all the mocked students have been added to the database here
        self.assertNotEqual(result1, "Student registration failed")
        self.assertNotEqual(result2, "Student registration failed")
        self.assertNotEqual(result3, "Student registration failed")
        self.assertNotEqual(result4, "Student registration failed")
        self.assertEqual( self.statistics.get_grade_mean_by_name("Yacine"),  mean)