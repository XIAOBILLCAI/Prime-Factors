import pytest
from prime import generate_prime_factors


def test_non_integer_input_raises_value_error():
    with pytest.raises(ValueError):
        generate_prime_factors("hello")

def test_one_returns_empty_list():
    assert generate_prime_factors(1) == []

def test_two_returns_two():
    assert generate_prime_factors(2) == [2]

def test_three_returns_three():
    assert generate_prime_factors(3) == [3]

def test_four_returns_two_twos():
    assert generate_prime_factors(4) == [2, 2]

def test_six_returns_two_and_three():
    assert generate_prime_factors(6) == [2, 3]


def test_eight_returns_three_twos():
    assert generate_prime_factors(8) == [2, 2, 2]
