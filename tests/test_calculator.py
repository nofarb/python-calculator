# tests/test_calculator.py
import pytest
from app.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
