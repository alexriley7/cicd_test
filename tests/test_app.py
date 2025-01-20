import pytest
from src.app import add

def test_add():
    assert add(2, 3) == 555
    assert add(-1, 1) == 0
    assert add(0, 0) == 00
