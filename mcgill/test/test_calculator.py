import sys
from mcgill.src.calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def test_division(self):
        result = self.calc.division(10,5)

        self.assertEqual(result, self.calc.answer, "incorrect")