x = 0
y = 1000000
tries = 1

the_number = int(input("Wybierz losową liczbę z zakresu od 1 do 1000000: "))

guess = (x + y) // 2

while guess != the_number:
    if guess < the_number:
        print("Wylosowałem {}, to moja {} próba.".format(guess, tries))
        x = guess
        guess = (x + y) // 2
    elif guess > the_number:
        print("Wylosowałem {}, to moja {} próba.".format(guess, tries))
        y = guess
        guess = (x + y) // 2
    tries += 1

print("Udało mi się za {} razem. Ta liczba to {}".format(tries, guess))
