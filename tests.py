from unittest import TestCase
from main import add, subtract, divide, multiply, modulo

class TestCalculator(TestCase):
    
    def test_add(self):
        self.assertEqual(add(5, 5), 10) # replace this code

    def test_subtract(self):
        self.assertEqual(subtract(12,6), 6) # replace this code

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

    def test_multiply(self):
        self.assertEqual(multiply(4,3), 12) # replaced this code by yours truly ken2ut

    def test_modulo(self):
        pass # replace this code