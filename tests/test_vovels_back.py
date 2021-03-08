from Codewars.vowels_back import vowel_back
import pytest

parameters = [
    ("testcase", "tabtbvba"),
    ("codewars", "bnaafvab"),
    ("exampletesthere", "agvvyuatabtqaaa")
]


@pytest.mark.parametrize("string, expected", parameters)
def test_vovel_back(string, expected):
    assert vowel_back(string) == expected
