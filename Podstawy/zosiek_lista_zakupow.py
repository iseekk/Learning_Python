import sys
from os import system

PRODUCTS = {'banan': 4, 'mleko': 2, 'chleb': 1}


def add_to_list(product, its_amount):
    if not product.isalpha() or not its_amount.isnumeric():
        raise ValueError('Bad value product or amount')
    else:
        its_amount = int(its_amount)
        product = product.lower()
        to_add = {product: its_amount + PRODUCTS.get(product)} if product in PRODUCTS else {product: its_amount}
        PRODUCTS.update(to_add)
        print("Dodano {amount} szt. {prod}".format(amount=its_amount, prod=product))


def list_view():
    print("Lista zakupow:")
    for number, item in enumerate(PRODUCTS, 1):
        amount = PRODUCTS.get(item)
        print("{number}. {prod}: {amount} szt.".format(number=number, prod=item, amount=amount))


def get_values():
    p = str(input("Podaj produkt:"))
    a = str(input("Podaj ilość:"))
    try:
        add_to_list(p, a)
    except ValueError as ex:
        print(str(ex))


def program_exit():
    sys.exit()


def bad_decision():
    print('Wybierz wlaściwą opcję z MENU!')


def print_menu():
    print("\nMENU\n"
          "1. Dodaj produkt\n"
          "2. Pokaż listę zakupów\n"
          "-----------------------\n"
          "5. Zamknij program")


SWITCH = {1: get_values,
          2: list_view,
          5: program_exit,
          }
if __name__ == '__main__':

    while True:
        system('cls')
        print_menu()
        try:
            key = int(input())
        except ValueError:
            print('Opcje w menu wybierz za pomocą liczb')
        else:
            SWITCH.get(key, bad_decision)()
        finally:
            input("\nAby kontynuować, naciśnij ENTER:")