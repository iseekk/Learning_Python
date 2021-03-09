import sys


def get_numbers():
    try:
        global x, y
        x = int(input("Podaj 1 liczbę:"))
        y = int(input("Podaj 2 liczbę:"))
    except ValueError:
        print(ValueError('\nMusisz wprowadzić liczbę!\n'))
        get_numbers()


def program_exit():
    sys.exit()


def bad_decision():
    print('Wybierz wlaściwą opcję z MENU!')


def print_menu():
    print("\nMENU\n"
          "1. Dodaj\n"
          "2. Odejmij\n"
          "3. Pomnóż\n"
          "4. Podziel\n"
          "-----------------------\n"
          "5. Zamknij program")


def dodaj():
    print("Suma liczb {} oraz {} to: {}".format(x, y, x + y))


def odejmij():
    print("Różnica liczb {} oraz {} to: {}".format(x, y, x - y))


def pomnoz():
    print("Iloczyn liczb {} oraz {} to: {}".format(x, y, x * y))


def podziel():
    if y == 0:
        print("Nie dzielimy przez 0")
    else:
        print("Iloraz liczb {} oraz {} to: {}".format(x, y, x / y))


SWITCH = {1: dodaj,
          2: odejmij,
          3: pomnoz,
          4: podziel,
          5: program_exit,
          }
if __name__ == '__main__':

    while True:
        get_numbers()
        print_menu()
        try:
            key = int(input())
        except ValueError:
            print('Opcje w menu wybierz za pomocą liczb')
        else:
            SWITCH.get(key, bad_decision)()
        finally:
            input("\nAby kontynuować, naciśnij ENTER:")
