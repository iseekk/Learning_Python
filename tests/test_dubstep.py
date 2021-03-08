from Codewars import dubstep as d
import pytest

params_pass = [
    ("WUBAWUBBWUBC", "A B C"),
    ("WUBABCWUBDEFWUBWUBGHI", "ABC DEF GHI"),
    ("WUBAWUB", "A")
]

params_false = [
    ("WUBAWUBBWUBC", " A B C "),
    ("WUBABCWUBDEFWUBWUBGHI", "ABCDEFGHI"),
    ("WUBAWUB", " A ")
]


@pytest.mark.parametrize("t_input, expected", params_pass)
def test_dubstep_pass(t_input, expected):
    assert d.dubstep(t_input) == expected


@pytest.mark.parametrize("test_input, expected", params_false)
def test_dubstep_false(test_input, expected):
    assert d.dubstep(test_input) != expected
