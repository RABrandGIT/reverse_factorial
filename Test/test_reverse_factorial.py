import pytest
from reverse_factorial import reverse_factorial

def test_reverse_factorial():
    assert reverse_factorial.reverse_factorial(120) == 5

def test_reverse_factorial():
    assert reverse_factorial.reverse_factorial(150) == None

def test_reverse_factorial():
    assert reverse_factorial.reverse_factorial(24) == 4
