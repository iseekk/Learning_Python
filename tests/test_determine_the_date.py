from Codewars.determine_the_date import get_day
import pytest

params = [
    (60, False, "March, 1"),
    (60, True, "February, 29"),
    (365, False, "December, 31"),
    (366, True, "December, 31"),
]


@pytest.mark.parametrize("arg, leap, expected", params)
def test_get_day(arg, leap, expected):
    assert get_day(arg, leap) == expected
