# stałe globalne
X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'TIE'
NUM_SQUARES = 9


# funkcje
def display_instructions():
    """Wyświetla instrukcję gry"""
    print(
        """
    Witaj w grze 'Kółko i krzyżyk'.
    Swój ruch wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
    Liczba odpowiada pozycji na planszy zgodnie z poniższym schematem:
     
            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8
            
    Powodzenia. \n
    """
    )


def ask_yes_no(question):
    """Zadaje pytanie, na które można odpowiedzieć tak lub nie"""
    response = None
    while response not in ('t', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Prosi o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print('Spróbuj ponownie...')
    return response


def pieces():
    """Ustala kto zaczyna pierwszy"""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n):")
    if go_first == 't':
        print('Pierwszy ruch należy do Ciebie.')
        computer = O
        human = X
    if go_first == 'n':
        print('Komputer wykonuje pierwszy ruch.')
        computer = X
        human = O
    return computer, human


def new_board():
    """Tworzy nową planszę gry"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Wyświetla planszę gry"""
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t-----------')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t-----------')
    print('\t', board[6], '|', board[7], '|', board[8], '\n')


def legal_moves(board):
    """Tworzy listę prawidłowych ruchów"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Ustala zwyciężcę gry"""
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board):
    """Odczytuje ruch gracza"""
    legal = legal_moves(board)
    move = None

    while move not in legal:
        move = ask_number('Jaki będzie twój ruch? (0-8):', 0, NUM_SQUARES)
        if move not in legal:
            print('\nTo pole jest już zajęte. Wybierz inne.\n')
    return move


def computer_move(board, computer, human):
    """Wykonuje ruch komputera"""
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    COUNTERMOVES = (1, 3, 5, 7)
    POSITIONS_TO_COUNTER = ((0, 8), (2, 6))

    print('Komputer wybiera pole numer', end=' ')

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for row in POSITIONS_TO_COUNTER:
        if board[row[0]] == human and board[row[1]] == human:
            for move in COUNTERMOVES:
                if move in legal_moves(board):
                    print(move)
                    return move

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Zmienia wykonawcę ruchu"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Ogłasza zwyciężcę gry"""
    if the_winner != TIE:
        print(the_winner, 'jest zwyciężcą!\n')
    else:
        print('Remis!\n')

    if the_winner == computer:
        print("Komputer wygrał!!!")
    elif the_winner == human:
        print("Wygrałeś!!!")


def main():
    """Wywołuje główną część programu"""
    computer, human = pieces()
    board = new_board()
    display_board(board)
    turn = X
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# początek programu
if __name__ == "__main__":
    display_instructions()
    while True:
        main()
        rematch = ask_yes_no('\nCzy chcesz zagrać ponownie? (t/n):')
        if rematch == 'n':
            break
    input("Koniec programu. Wciśnij Enter aby zakończyć.")
