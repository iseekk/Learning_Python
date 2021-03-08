# To pierwsza próba stworzenia gry, w której komputer próbuje
# odgadnąć wprowadzoną liczbę.

import random

x = 1
y = 1000000
guess = random.randint(x, y)
tries = 1

the_number = int(input("Wybierz losową liczbę z zakresu od 1 do 1000000: "))

while guess != the_number:
    if guess < the_number:
        print("Wylosowałem {}. To moja {} próba.".format(guess, tries))
        x = guess + 1
        guess = random.randint(x, y)
    elif guess > the_number:
        print("Wylosowałem {}. To moja {} próba.".format(guess, tries))
        y = guess - 1
        guess = random.randint(x, y)
    tries += 1

print("Udało mi się zgadnąć za {} razem. Ta liczba to {}".format(tries, guess))
