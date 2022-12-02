from mcgill.src.db.sql_create import Creation


class Sorting:

    def __init__(self) -> None:
        pass

    def sortStudentsByGrade(self, studentName):
        student_list = Creation().get_students_by_name(studentName)
        student_list.sort(key = lambda x: x.grade)
        return student_list

    def sortStudentsByName(self, studentName):
        student_list = Creation().get_students_by_name(studentName)
        student_list.sort(key = lambda x: x.name)
        return student_list


    def sortStudentsByAge(self, studentName):
        student_list = Creation().get_students_by_name(studentName)
        student_list.sort(key = lambda x: x.age)
        return student_list

    def sortStudentsByMajor(self, studentName):
        student_list = Creation().get_students_by_name(studentName)
        student_list.sort(key = lambda x: x.major)
        return student_list






    
