from Codewars import football as fb
import pytest


params = [
    (["A4Y", "A4Y"], (10, 11)),
    ([], (11, 11))
]


@pytest.mark.parametrize("inp,exp", params)
def test_men_still_standing(inp, exp):
    assert fb.men_still_standing(inp) == exp

