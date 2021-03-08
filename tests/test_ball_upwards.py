from Codewars.ball_upwards import max_ball
import pytest


parameters = [
    (37, 10),
    (45, 13),
    (99, 28),
    (85, 24)
]


@pytest.mark.parametrize("arg, expected", parameters)
def test_max_ball(arg, expected):
    assert max_ball(arg) == expected
