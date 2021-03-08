from Codewars.prime_product import is_prime, prime_product
import pytest

is_prime_params = [
    (11, True),
    (61, True),
    (1619, True),
    (10, False),
    (213, False),
    (1617, False),
]


@pytest.mark.parametrize("arg, expected", is_prime_params)
def test_is_prime(arg, expected):
    assert is_prime(arg) == expected


prime_product_params = [
    (9, 14),
    (10, 25),
    (11, 0),
    (12, 35),
    (20, 91),
    (100, 2491),
]


@pytest.mark.parametrize("arg, expected", prime_product_params)
def test_prime_product(arg, expected):
    assert prime_product(arg) == expected