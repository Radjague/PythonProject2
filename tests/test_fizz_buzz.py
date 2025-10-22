import pytest

from src.fizz_buzz import fizz_buzz

@pytest.mark.parametrize('n,expected_result', [(0,'fizzbuzz'), (1,'1'), (2,'2')])

def test_n_returns_expected_result(n,expected_result):
     actual_result = fizz_buzz(n)
     assert actual_result == expected_result