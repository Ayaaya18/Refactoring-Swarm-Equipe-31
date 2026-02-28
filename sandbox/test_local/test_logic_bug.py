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

def test_count_down_invalid_input_type():
    with pytest.raises(ValueError):
        count_down("five")

def test_count_down_invalid_input_type_with_print_statement():
    with pytest.raises(ValueError):
        print(count_down("five"))

def test_count_down_large_number():
    count_down(1000)
    assert True

def test_count_down_zero_with_print_statement():
    with pytest.raises(ValueError):
        print(count_down(0))

def test_count_down_negative_integer_with_print_statement():
    with pytest.raises(ValueError):
        print(count_down(-1))

def test_count_down_non_integer_with_print_statement():
    with pytest.raises(ValueError):
        print(count_down(3.5))

def test_count_down_invalid_input_type_with_print_statement_and_assignment():
    with pytest.raises(ValueError):
        result = count_down("five")
        print(result)

def test_count_down_invalid_input_type_with_print_statement_and_assignment_and_print():
    with pytest.raises(ValueError):
        result = count_down("five")
        print(result)
