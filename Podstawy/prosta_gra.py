import gry, random

again = None
while again != 'n':
    players = []
    num = gry.ask_number(question='Podaj liczbę graczy. (2-5):', low=2, high=5)
    for i in range(num):
        name = input("Podaj imię gracza numer {pl_num}".format(pl_num=i+1))
        score = random.randrange(100) + 1
        player = gry.Player(name, score)
        players.append(player)
    print('Wyniki gry:')
    for player in players:
        print(player)
    again = gry.ask_yes_no("Czy chcesz zagrać ponownie? (t/n):")