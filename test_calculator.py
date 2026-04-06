import pytest
from calculator import calculate

# ── Basic Operations ──────────────────────────────────────

def test_addition():
    assert calculate(2, '+', 3) == 5

def test_subtraction():
    assert calculate(10, '-', 4) == 6

def test_multiplication():
    assert calculate(3, '*', 7) == 21

def test_division():
    assert calculate(10, '/', 2) == 5.0

# ── Edge Cases ────────────────────────────────────────────

def test_divide_by_zero():
    assert calculate(5, '/', 0) == "Error: Cannot divide by zero!"

def test_negative_sqrt():
    assert calculate(-9, 'sqrt') == "Error: Cannot square root a negative number!"

def test_invalid_operator():
    assert calculate(2, '?', 3) == "Error: Invalid operator!"

# ── New Features ──────────────────────────────────────────

def test_power():
    assert calculate(2, '^', 10) == 1024

def test_square_root():
    assert calculate(9, 'sqrt') == 3.0

def test_float_addition():
    assert calculate(0.1, '+', 0.2) == pytest.approx(0.3)