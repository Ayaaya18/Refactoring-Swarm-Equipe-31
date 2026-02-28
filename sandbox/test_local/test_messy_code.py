# test_messy_code.py

import pytest
from messy_code import *

def test_f_within_range():
    # Test case: number within range
    assert f(50) == True

def test_f_at_max_value():
    # Test case: number at max value
    assert f(MAX_VALUE) == True

def test_f_at_min_value():
    # Test case: number at min value (0)
    assert f(0) == False

def test_f_below_min_value():
    # Test case: number below min value
    assert f(-1) == False

def test_f_above_max_value():
    # Test case: number above max value
    assert f(101) == False

def test_f_non_integer_input():
    # Test case: non-integer input
    with pytest.raises(TypeError):
        f(50.5)

def test_f_non_numeric_input():
    # Test case: non-numeric input
    with pytest.raises(TypeError):
        f('a')
