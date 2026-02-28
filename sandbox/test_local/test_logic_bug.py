# test_logic_bug.py
import pytest
from logic_bug import *

def test_count_down_positive_integer():
    count_down(5)
    assert True

def test_count_down_zero():
    with pytest.raises(ValueError):
        count_down(0)

def test_count_down_negative_integer():
    with pytest.raises(ValueError):
        count_down(-1)

def test_count_down_non_integer():
    with pytest.raises(ValueError):
        count_down(3.5)

def test_count_down_large_number():
    count_down(1000)
    assert True

def test_count_down_single_digit():
    count_down(9)
    assert True

def test_count_down_zero_with_assert():
    try:
        count_down(0)
        assert False, "Expected ValueError to be raised"
    except ValueError:
        assert True

def test_count_down_negative_integer_with_assert():
    try:
        count_down(-1)
        assert False, "Expected ValueError to be raised"
    except ValueError:
        assert True

def test_count_down_non_integer_with_assert():
    try:
        count_down(3.5)
        assert False, "Expected ValueError to be raised"
    except ValueError:
        assert True
