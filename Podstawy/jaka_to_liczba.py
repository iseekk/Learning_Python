import random


# wartości początkowe
LOW = 1
HIGH = 100
TRIES_LIMIT = 10


def display_instructions():
    print("\n\tWitaj w grze 'Jaka to liczba'!")
    print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
    print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")


def ask_number(question, LOW, HIGH):
    """Prosi o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(LOW, HIGH):
        try:
            response = int(input(question))
        except ValueError:
            print("To nie jest liczba.")
    return response


def main():
    # początek programu
    the_number = random.randint(LOW, HIGH + 1)
    tries = 1
    guess = ask_number("Ta liczba to: ", LOW, HIGH + 1)
    # pętla zgadywania
    while guess != the_number and tries < TRIES_LIMIT:
        if guess > the_number:
            print("Za duża...")
        else:
            print("Za mała...")
        guess = ask_number("Ta liczba to: ", LOW, HIGH + 1)
        tries += 1

    if tries < TRIES_LIMIT:
        print("Odgadłeś! Ta liczba to", the_number)
        print("Do osiągnięcia sukcesu potrzebowałeś", tries, "prób!\n")
    else:
        print("\nPrzekroczyłeś limit prób!")


# początek programu
display_instructions()
main()
