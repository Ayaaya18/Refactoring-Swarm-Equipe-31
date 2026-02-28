# bad_syntax.py

def calculate_sum_of_two_numbers(a: int, b: int) -> int:
    """
    Calculate the sum of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b

# test_bad_syntax.py

import unittest

class TestCalculateSumOfTwoNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_sum_of_two_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(calculate_sum_of_two_numbers(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(calculate_sum_of_two_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
