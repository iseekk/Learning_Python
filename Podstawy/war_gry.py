class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        return "{name}:\t{score}".format(name=self.name, score=self.score)


def ask_yes_no(question):
    response = None
    while response not in ('t', 'n'):
        try:
            response = input(question).lower()
        except ValueError:
            continue
    return response


def ask_number(question, low, high):
    response = None
    while response not in (range(low, high + 1)):
        try:
            response = int(input(question))
        except ValueError:
            continue
    return response


if __name__ == '__main__':
    print('Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).')
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")