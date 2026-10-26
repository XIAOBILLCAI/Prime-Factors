
"""Tests for the prime factor generation function."""

import pytest
from prime import generate_prime_factors


def test_non_integer_input_raises_value_error():
    """Check that non-integer input raises ValueError."""
    with pytest.raises(ValueError):
        generate_prime_factors("hello")

def test_one_returns_empty_list():
    """Check that 1 returns an empty list."""
    assert not generate_prime_factors(1)

def test_two_returns_two():
    """Check that 2 returns [2]."""
    assert generate_prime_factors(2) == [2]

def test_three_returns_three():
    """Check that 3 returns [3]."""
    assert generate_prime_factors(3) == [3]

def test_four_returns_two_twos():
    """Check that 4 returns [2, 2]."""
    assert generate_prime_factors(4) == [2, 2]

def test_six_returns_two_and_three():
    """Check that 6 returns [2, 3]."""
    assert generate_prime_factors(6) == [2, 3]


def test_eight_returns_three_twos():
    """Check that 8 returns [2, 2, 2]."""
    assert generate_prime_factors(8) == [2, 2, 2]


def test_nine_returns_two_threes():
    """Check that 9 returns [3, 3]."""
    assert generate_prime_factors(9) == [3, 3]

def test_twelve_returns_two_twos_and_three():
    """Check that 12 returns [2, 2, 3]."""
    assert generate_prime_factors(12) == [2, 2, 3]
