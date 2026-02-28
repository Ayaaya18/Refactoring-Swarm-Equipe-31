"""
Module to test the calculate_sum function.

This module contains unit tests for the calculate_sum function.
"""

import unittest

def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a + b

class TestCalculateSum(unittest.TestCase):
    """
    Test class for the calculate_sum function.
    """

    def test_positive_numbers(self):
        """
        Test the calculate_sum function with positive numbers.
        """
        self.assertEqual(calculate_sum(1, 2), 3)

    def test_negative_numbers(self):
        """
        Test the calculate_sum function with negative numbers.
        """
        self.assertEqual(calculate_sum(-1, -2), -3)

    def test_zero(self):
        """
        Test the calculate_sum function with zero.
        """
        self.assertEqual(calculate_sum(0, 0), 0)

    def test_none_inputs(self):
        """
        Test the calculate_sum function with None inputs.
        """
        with self.assertRaises(TypeError):
            calculate_sum(1, None)

    def test_large_numbers(self):
        """
        Test the calculate_sum function with very large numbers.
        """
        self.assertEqual(calculate_sum(10**100, 10**100), 2 * 10**100)

    def test_invalid_types(self):
        """
        Test the calculate_sum function with invalid types.
        """
        with self.assertRaises(TypeError):
            calculate_sum('a', 2)

    def test_invalid_number_of_args(self):
        """
        Test the calculate_sum function with an invalid number of arguments.
        """
        with self.assertRaises(TypeError):
            calculate_sum(1)

    def test_invalid_input(self):
        """
        Test the calculate_sum function with an invalid input.
        """
        with self.assertRaises(TypeError):
            calculate_sum([1, 2], 3)

    def test_floats(self):
        """
        Test the calculate_sum function with floats.
        """
        self.assertEqual(calculate_sum(1.5, 2.5), 4.0)

    def test_negative_floats(self):
        """
        Test the calculate_sum function with negative floats.
        """
        self.assertEqual(calculate_sum(-1.5, -2.5), -4.0)

    def test_zero_floats(self):
        """
        Test the calculate_sum function with zero floats.
        """
        self.assertEqual(calculate_sum(0.0, 0.0), 0.0)

if __name__ == '__main__':
    """
    Run the unit tests.
    """
    unittest.main()
