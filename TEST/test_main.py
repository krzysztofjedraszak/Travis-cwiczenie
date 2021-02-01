import pytest
import main

def test_suma1():
    a=0
    b=10

    out=main.suma(a,b)
    assert out==10


def test_suma2():
    a = 5
    b = 100

    out = main.suma(a, b)
    assert out == 105


def test_roznica1():
    a = 0
    b = 10

    out = main.roznica(a, b)
    assert out == -10

def test_roznica2():
    a = 550
    b = 10

    out = main.roznica(a, b)
    assert out == 540

