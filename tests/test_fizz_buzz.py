from src.fizz_buzz import fizz_buzz


def test_0_returns_fizz_buzz():
    assert fizz_buzz(0) == 'fizzbuzz'

def test_1_returns_1():
    assert fizz_buzz(1) == '1'