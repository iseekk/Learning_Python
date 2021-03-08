import random

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
"""
)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("NADUŻYWANY", "MAŁŻ", "GUMA", "NAFTA", "PYTHON")

word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("\nWitaj w grze 'Szubienica'. Powodzenia!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystałeś już następujące litery: \n", used)
    print("\nZagadkowe słowo:\n", so_far)

    guess = input("\nPodaj literę:")
    guess = guess.upper()
    while guess in used:
        guess = input("\nUżyłeś już tej litery, podaj inną:")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\nZgadłeś jedną z liter tajemniczego wyrazu!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nNiestety, ta litera nie występuje w tajemniczym wyrazie :(")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nPRZEGRAŁEŚ! Zostałeś powieszony")
else:
    print("\nWYGRAŁEŚ!")

print("\nZagadkowe słowo to:", word)

input("\n\nNaciśnij Enter, aby zakończyć program...")
