import Podstawy.kolkokrzyzyk as k
import mock
import pytest

O = "O"
X = "X"
E = " "
T = "TIE"
INCORRECT_INPUT = ["a", "1", "!", "", " "]
CORRECT_VALUES = [(2, 1, 3), (5, 1, 10)]
INCORECT_VALUES = [("", 1, 3), ("w", 2, 5), (".", 0, 120)]
PIECES = [("t", O, X), ("n", X, O), ]
PROPER_BOARD = [E]*9
DISPLAY_BOARD = [O, O, O, X, X, X, E, E, E]
DISPLAY_BOARD_EXCPECTED = f'\n\t {O} | {O} | {O}\n\t-----------\n' \
                          f'\t {X} | {X} | {X}\n\t-----------\n' \
                          f'\t {E} | {E} | {E} \n\n'

BOARD_MOVES = [
    ([E, X, X, O, O, O, X, E, X], [0, 7]),
    ([E, X, E, O, X, O, O, X, E], [0, 2, 8]),
    ([X, O, X, O, X, O, O, X, O], []),
]

WINNER_BOARDS = [
    ([E, X, X, O, O, O, X, E, X], O),
    ([E, X, E, O, X, O, O, X, E], X),
    ([X, O, X, O, X, O, O, X, O], T),
    ([X, O, E, E, E, E, E, E, E], None)
]
HUMAN_MOVES = [(0, [E, X, X, O, O, O, X, E, X], 0)]


@pytest.mark.parametrize("user_input", ["t", "n"])
def test_askyn_correct(user_input):
    with mock.patch('builtins.input', return_value=user_input):
        assert k.ask_yes_no("question") == user_input


@pytest.mark.parametrize("user_input", INCORRECT_INPUT)
def test_askyn_wrong(user_input):
    with mock.patch('builtins.input', return_value=user_input):
        assert not k.ask_yes_no("question")


@pytest.mark.parametrize("user_input,low,high", CORRECT_VALUES)
def test_asknum_correct(user_input, low, high):
    with mock.patch('builtins.input', return_value=user_input):
        assert k.ask_number("bla bla", low, high) == user_input


@pytest.mark.parametrize("user_input,low,high", INCORECT_VALUES)
def test_asknum_wrong(user_input, low, high):
    with mock.patch('builtins.input', return_value=user_input):
        assert not k.ask_number("bla bla", low, high)


@pytest.mark.parametrize("user_input,computer,human", PIECES)
def test_pieces(user_input, computer, human):
    with mock.patch('builtins.input', return_value=user_input):
        assert k.pieces() == (computer, human)


def test_new_board():
    assert k.new_board() == PROPER_BOARD


def test_display_board(capsys):
    k.display_board(DISPLAY_BOARD)
    captured = capsys.readouterr()
    assert captured.out == DISPLAY_BOARD_EXCPECTED




@pytest.mark.parametrize("board,moves", BOARD_MOVES)
def test_legal_moves(board, moves):
    assert k.legal_moves(board) == moves



@pytest.mark.parametrize("board,winner", WINNER_BOARDS)
def test_winner(board, winner):
    assert k.winner(board) == winner


@pytest.mark.parametrize("user_input,board,result", HUMAN_MOVES)
def test_human_move(user_input, board, result):
    with mock.patch('builtins.input', return_value=user_input):
        assert k.human_move(board) == result