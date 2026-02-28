"""
Module to demonstrate a countdown function.
"""

def count_down(n):
    """
    Prints a countdown from n to 1.

    Args:
        n (int): The starting number for the countdown.

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

if __name__ == '__main__':
    unittest.main()
