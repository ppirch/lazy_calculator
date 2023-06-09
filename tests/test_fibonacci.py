# Desc: Tests for fibonacci.py

import pytest
from lazy_calculator import fibonacci


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040


def test_fibonacci_large():
    assert fibonacci(50) == 12586269025
    assert fibonacci(60) == 1548008755920
    assert fibonacci(70) == 190392490709135
    assert fibonacci(80) == 23416728348467685
    assert fibonacci(90) == 2880067194370816120
    assert fibonacci(100) == 354224848179261915075


def test_fibonacci_f0():
    assert fibonacci(0, f0=1, f1=1) == 1
    assert fibonacci(1, f0=1, f1=1) == 1
    assert fibonacci(5, f0=1, f1=1) == 8
    assert fibonacci(10, f0=1, f1=1) == 89
    assert fibonacci(20, f0=1, f1=1) == 10946
    assert fibonacci(30, f0=1, f1=1) == 1346269


def test_fibonacci_f1():
    assert fibonacci(0, f0=0, f1=2) == 0
    assert fibonacci(1, f0=0, f1=2) == 2
    assert fibonacci(5, f0=0, f1=2) == 10
    assert fibonacci(10, f0=0, f1=2) == 110
    assert fibonacci(20, f0=0, f1=2) == 13530
    assert fibonacci(30, f0=0, f1=2) == 1664080


def test_fibonacci_f0_f1():
    assert fibonacci(0, f0=2, f1=3) == 2
    assert fibonacci(1, f0=2, f1=3) == 3
    assert fibonacci(5, f0=2, f1=3) == 21
    assert fibonacci(10, f0=2, f1=3) == 233
    assert fibonacci(20, f0=2, f1=3) == 28657
    assert fibonacci(30, f0=2, f1=3) == 3524578
