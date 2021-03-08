import random

WORDS = ("hipopotam", "surykatka", "tygrys",
         "żyrafa", "zebra", "jaguar", "gepard",
         "orangutan", "nosorożec", "guziec")

word = random.choice(WORDS)
hint = ""

print("\nWylosowane przeze mnie słowo ma {} liter. Zgadnij jakie to słowo.".format(len(word)))
print("Wprowadź literę, a powiem ci czy jest ona zawarta w tym słowie. Masz pięć szans.")

for i in range(5):
    letter = input("Podaj {}. literę: ".format(i+1))
    if letter in word:
        print("TAK")
        hint += letter
    else:
        print("NIE")

print("\nLitery zawarte w słowie: {}".format(hint))

guess = input("\nTe słowo to: ")

if guess == word:
    print("Odgadłeś!")
else:
    print("Nie udało ci się! :)")