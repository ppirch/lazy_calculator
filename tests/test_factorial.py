# Desc: Tests for factorial.py

import pytest
from lazy_calculator.factorial import factorial


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000


def test_factorial_large():
    assert factorial(30) == 265252859812191058636308480000000
    assert factorial(40) == 815915283247897734345611269596115894272000000000
    assert factorial(50) == 30414093201713378043612608166064768844377641568960512000000000000
