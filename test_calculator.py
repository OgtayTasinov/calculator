import pytest
import calculator
# from  calculator import * {or add, subtract, multiply, divide}

def test_add():
    assert calculator.add(1, 1) == 2
def test_subtract():
    assert calculator.subtract(5, 1) == 4
    # assert calculator.subtract(3, 3) == 100
def test_multiply():
    assert calculator.multiply(3, 3) == 9
def test_divide():
    assert calculator.divide(9, 3) == 3