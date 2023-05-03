from unittest import TestCase
from main import add, subtract, divide, multiply, modulo

class TestCalculator(TestCase):
    
    def test_add(self):
        pass # replace this code

    def test_subtract(self):
        pass # replace this code

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

    def test_multiply(self):
        pass # replace this code

    def test_modulo(self):
        pass # replace this code