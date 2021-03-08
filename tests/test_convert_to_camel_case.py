from Codewars.convert_to_camel_case import to_camel_case
import pytest

params = [
    ("the_stealth_warrior", "theStealthWarrior"),
    ("The-Stealth-Warrior", "TheStealthWarrior"),
]


@pytest.mark.parametrize("arg, expected", params)
def test_to_camel_case(arg, expected):
    assert to_camel_case(arg) == expected