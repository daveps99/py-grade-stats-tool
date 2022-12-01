

class Calculator(object):
    '''
    Calculator app used for statistical computations of the student grades.
    '''
    def __init__(self):
        self.answer = 0

    def addition(self,a,b):
        self.answer = a+b
        return self.answer

    def substraction(self,a,b):
        self.answer = a-b
        return self.answer

    def multiplication(self,a,b):
        self.answer = a*b
        return self.answer

    def division(self,a,b):
        self.answer = a/b
        return self.answer