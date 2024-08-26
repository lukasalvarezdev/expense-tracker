import unittest

from helpers import (
    add,
    divide,
    do,
    is_number,
    is_operation,
    multiply,
    should_get_result,
    subtract,
)


class TestCalculatorFunctions(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(is_number("5"))
        self.assertTrue(is_number("3.14"))
        self.assertFalse(is_number("abc"))
        self.assertFalse(is_number("*"))

    def test_is_operation(self):
        self.assertTrue(is_operation("+"))
        self.assertTrue(is_operation("-"))
        self.assertTrue(is_operation("*"))
        self.assertTrue(is_operation("/"))
        self.assertFalse(is_operation("="))
        self.assertFalse(is_operation("5"))

    def test_should_get_result(self):
        self.assertTrue(should_get_result("="))
        self.assertFalse(should_get_result("+"))
        self.assertFalse(should_get_result("5"))

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(5, 0), "Error: Division by zero")

    def test_do(self):
        self.assertEqual(do(2, 3, "+"), 5)
        self.assertEqual(do(5, 3, "-"), 2)
        self.assertEqual(do(2, 3, "*"), 6)
        self.assertEqual(do(6, 3, "/"), 2)
        with self.assertRaises(Exception):
            do(5, 3, "^")


if __name__ == "__main__":
    unittest.main()
