# test_bad_syntax.py
import pytest
from bad_syntax import *

def test_calculate_sum_positive_numbers():
    """
    Test the calculate_sum function with positive numbers.
    """
    assert calculate_sum(1, 2) == 3

def test_calculate_sum_negative_numbers():
    """
    Test the calculate_sum function with negative numbers.
    """
    assert calculate_sum(-1, -2) == -3

def test_calculate_sum_zero():
    """
    Test the calculate_sum function with zero.
    """
    assert calculate_sum(0, 0) == 0

def test_calculate_sum_none_inputs():
    """
    Test the calculate_sum function with None inputs.
    """
    with pytest.raises(TypeError):
        calculate_sum(1, None)

def test_calculate_sum_large_numbers():
    """
    Test the calculate_sum function with very large numbers.
    """
    assert calculate_sum(10**100, 10**100) == 2 * 10**100

def test_calculate_sum_invalid_types():
    """
    Test the calculate_sum function with invalid types.
    """
    with pytest.raises(TypeError):
        calculate_sum('a', 2)

def test_calculate_sum_invalid_number_of_args():
    """
    Test the calculate_sum function with an invalid number of arguments.
    """
    with pytest.raises(TypeError):
        calculate_sum(1)

def test_calculate_sum_invalid_input():
    """
    Test the calculate_sum function with an invalid input.
    """
    with pytest.raises(TypeError):
        calculate_sum([1, 2], 3)

def test_calculate_sum_floats():
    """
    Test the calculate_sum function with floats.
    """
    assert calculate_sum(1.5, 2.5) == 4.0

def test_calculate_sum_negative_floats():
    """
    Test the calculate_sum function with negative floats.
    """
    assert calculate_sum(-1.5, -2.5) == -4.0

def test_calculate_sum_zero_floats():
    """
    Test the calculate_sum function with zero floats.
    """
    assert calculate_sum(0.0, 0.0) == 0.0
