import sys
from mcgill.src.calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def test_division(self):
        result = self.calc.division(10,5)

        self.assertEqual(result, self.calc.answer, "incorrect")

    #this should fail the build since addition is not implemented
    def test_addition(self):
        result = self.calc.addition(10,5)

        self.assertEqual(result, self.calc.answer, "incorrect")