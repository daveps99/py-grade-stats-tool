from mcgill.src.db.sql_create import Creation

NAME_INDEX = 0
AGE_INDEX = 1
GRADE_INDEX = 2
MAJOR_INDEX = 3

class Sorting:

    def __init__(self) -> None:
        pass

    def sortStudentsByGrade(self, studentName):
        student_list = Creation().get_students_by_name(studentName)
        student_list.sort(key = lambda x: x[GRADE_INDEX])
        return student_list

    def sortStudentsByAge(self, studentName):
        student_list = Creation().get_students_by_name(studentName)
        student_list.sort(key = lambda x: x[AGE_INDEX])
        return student_list

    def sortStudentsByMajor(self, studentName):
        student_list = Creation().get_students_by_name(studentName)
        student_list.sort(key = lambda x: x[MAJOR_INDEX])
        return student_list






    
