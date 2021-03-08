import random

WORDS = ("python", "komputer", "rower", "programowanie")
HINTS = ("Język, którego obecnie używasz", "Inaczej PeCet", "Ma dwa koła", "Inaczej pisanie programów")
word = random.choice(WORDS)
correct = word
jumble = ""
counter = 0

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Zgadnij, jakie to słowo. Wpisz 'hint', aby zobaczyć podpowiedź (brak dodatkowych punktów).", jumble)

guess = input("Twoja odpowiedź: ")

while guess != correct and guess != "":
    if guess == "hint":
        counter += 1
        if correct == "python":
            print(HINTS[0])
        if correct == "komputer":
            print(HINTS[1])
        if correct == "rower":
            print(HINTS[2])
        if correct == "programowanie":
            print(HINTS[3])
        guess = input("Twoja odpowiedź: ")
    else:
        print("Niestety, nie zgadłeś!")
        guess = input("Twoja odpowiedź: ")

if guess == correct:
    print("Zgadłeś! Gratulacje!")
if counter == 0:
    print("Zdobyłeś dodatkowe punkty za nieskorzystanie z podpowiedzi!")

print(input("\nNaciśnij ENTER, aby zakończyć program:"))