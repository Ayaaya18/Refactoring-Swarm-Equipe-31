# test_bad_syntax_pytest.py

import pytest
from bad_syntax import *

def test_calculate_sum_of_two_numbers_positive_numbers():
    assert calculate_sum_of_two_numbers(2, 3) == 5

def test_calculate_sum_of_two_numbers_negative_numbers():
    assert calculate_sum_of_two_numbers(-2, -3) == -5

def test_calculate_sum_of_two_numbers_zero():
    assert calculate_sum_of_two_numbers(0, 0) == 0

def test_calculate_sum_of_two_numbers_mixed_numbers():
    assert calculate_sum_of_two_numbers(-2, 3) == 1

def test_calculate_sum_of_two_numbers_invalid_input_type():
    with pytest.raises(TypeError):
        calculate_sum_of_two_numbers('a', 3)

def test_calculate_sum_of_two_numbers_invalid_input_value():
    with pytest.raises(TypeError):
        calculate_sum_of_two_numbers(None, 3)

def test_calculate_sum_of_two_numbers_invalid_input_type_b():
    with pytest.raises(TypeError):
        calculate_sum_of_two_numbers(3, 'b')

def test_calculate_sum_of_two_numbers_invalid_input_value_b():
    with pytest.raises(TypeError):
        calculate_sum_of_two_numbers(3, None)