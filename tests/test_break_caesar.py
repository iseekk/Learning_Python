from Codewars.break_the_caesar import break_caesar
import pytest

params = [("DAM? DAM! DAM.", 7),
          ("Mjqqt, btwqi!", 5),
          ("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.", 13),
          ]


@pytest.mark.parametrize("arg, expected", params)
def test_func(arg, expected):
    assert break_caesar(arg) == expected
