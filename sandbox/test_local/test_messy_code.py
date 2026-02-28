# test_messy_code.py
import pytest
from messy_code import *

def test_f_inclusive_range():
    # Test that the function returns True for numbers within the inclusive range
    assert f(0) == True
    assert f(50) == True
    assert f(100) == True

def test_f_out_of_range():
    # Test that the function returns False for numbers outside the inclusive range
    assert f(-1) == False
    assert f(101) == False
    assert f(200) == False

def test_f_invalid_input():
    # Test that the function raises a TypeError for non-integer inputs
    with pytest.raises(TypeError):
        f(3.14)
    with pytest.raises(TypeError):
        f('hello')
