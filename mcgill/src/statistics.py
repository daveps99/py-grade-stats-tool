from mcgill.src.calculator import Calculator
from mcgill.src.db.sql_create import Creation

GRADE_INDEX = 2

class Statistics:

    def __init__(self) -> None:
        pass

    def get_grade_mean_by_name(self, name):
        student_list = Creation().get_students_by_name(name)
        sum = 0

        for student in student_list:
            grade = student[GRADE_INDEX]
            sum += grade

        return (sum/len(student_list))