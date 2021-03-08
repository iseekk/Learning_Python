import mock
from mock import Mock
import mim


@mock.patch.object(mim.Application, "get_random_person")
def test_get_next_person(mock_random):
    expected = "Katie"
    mock_random.return_value = expected
    user = {"people seen": ["Jane"]}
    ap = mim.Application()
    actual = ap.get_next_person(user)

    assert actual == expected


@mock.patch.object(mim.Application, "send_email")
@mock.patch.object(mim.Application, "let_down_gently")
@mock.patch.object(mim.Application, "give_it_time")
def test_evaluate_dislikes(mock_give_it_time,
                           mock_let_down_gently,
                           mock_send_email):
    person1 = "Zosiek"
    person2 = {"likes": ["Leavok", "Piper"],
               "dislikes": ["Zosiek"]}
    ap = mim.Application()
    ap.evaluate(person1, person2)

    mock_let_down_gently.assert_called_with(person1)
    assert mock_send_email.call_count == 0
    assert mock_give_it_time.call_count == 0


@mock.patch.object(mim.Application, "send_email")
def test_person2_likes_person1(mock_send_email):
    person1 = "Zosiek"
    person2 = {"likes": ["Zosiek"]}
    ap = mim.Application()
    ap.evaluate(person1, person2)

    call_1 = mock_send_email.call_args_list[0]
    call_2 = mock_send_email.call_args_list[1]

    assert call_1 == mock.call(person1)
    assert call_2 == mock.call(person2)


@mock.patch("builtins.open")
def test_open_file(mock_open):
    filename = "does_not_exist.json"
    mock_file = Mock()
    mock_open.return_value = mock_file
    mock_file.read.return_value = '{"foo": "bar"}'
    actual_result = mim.get_json(filename)
    assert actual_result == {"foo": "bar"}


@mock.patch("builtins.open")
def test_ioerror_exception(mock_open):
    filename = "does_not_exist.json"
    mock_open.side_effect = IOError
    actual_result = mim.get_json(filename)
    assert actual_result == ""


@mock.patch("json.loads")
@mock.patch("builtins.open")
def test_valerror_exception(mock_open, mock_loads):
    filename = "does_not_exist.json"
    mock_file = Mock()
    mock_file.read.return_value = '{"foo": "bar"}'
    mock_open.return_value = mock_file
    mock_loads.side_effect = ValueError
    actual_result = mim.get_json(filename)
    assert actual_result == ""
