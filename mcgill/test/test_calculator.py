from mcgill.src.calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.addition(10,5)

        self.assertEqual(result, self.calc.answer, "incorrect")    

    def test_substraction(self):
        result = self.calc.substraction(10,5)

        self.assertEqual(result, self.calc.answer, "incorrect")

    def test_multiplication(self):
        result = self.calc.multiplication(10,5)

        self.assertEqual(result, self.calc.answer, "incorrect")

    def test_division(self):
        result = self.calc.division(10,5)
        fail_result = self.calc.division(10,0)

        self.assertEqual(result, self.calc.answer, "incorrect")
        self.assertEqual(fail_result, "Cannot divide by 0")