from src.fizz_buzz import fizz_buzz


def test_fizz_buzz_function_is_callable():
    fizz_buzz(0)

def test_0_returns_fizz_buzz():
    assert fizz_buzz(0) == 'fizzbuzz'