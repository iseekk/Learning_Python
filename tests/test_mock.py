import mock
import mim


def ab():
    return 5


def test_display():
    a = 2
    b = 3
    with mock.patch("mim.plus", return_value=a + b):
        assert mim.display("test", a, b) == "test: 5"


@mock.patch("mim.plus")
def test_display_dec(mock_plus):
    mock_plus.return_value = 5
    assert mim.display("test", 2, 3)

