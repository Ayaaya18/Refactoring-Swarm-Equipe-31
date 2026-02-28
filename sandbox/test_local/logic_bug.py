"""
Module for counting down from a given number.

This module provides a function to count down from a given number.
"""

def count_down(n):
    """
    Counts down from a given number.

    Args:
        n (int): The number to count down from.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    while n > 0:
        print(n)
        n -= 1

import unittest

class TestCountDown(unittest.TestCase):
    def test_count_down_positive_integer(self):
        count_down(5)

    def test_count_down_zero(self):
        with self.assertRaises(ValueError):
            count_down(0)

    def test_count_down_negative_integer(self):
        with self.assertRaises(ValueError):
            count_down(-1)

    def test_count_down_non_integer(self):
        with self.assertRaises(ValueError):
            count_down(3.5)

    def test_count_down_invalid_input_type(self):
        with self.assertRaises(ValueError):
            count_down("five")

    def test_count_down_invalid_input_type_with_print_statement(self):
        with self.assertRaises(ValueError):
            print(count_down("five"))

if __name__ == '__main__':
    unittest.main()
