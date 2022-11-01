import pytest
from main import sumar, multiplicar

def test_sumar():
    assert sumar(2,3) == 5

def test_multiplicar():
    assert multiplicar(2,2) == 4