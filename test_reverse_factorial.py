import pytest
from reverse_factorial import factorial

def test1():
    assert factorial(120) == 5

def test2():
    assert factorial(720) == 6

def test3():
    assert factorial(24) == 4
