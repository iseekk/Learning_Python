import war_gry
import war_karty


class WarCard(war_karty.Card):
    @property
    def value(self):
        v = super(WarCard, self).value
        if v == 1:
            v = 14
        return v


class WarHand(war_karty.Hand):
    def __init__(self, name):
        super(WarHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ':\t' + super(WarHand, self).__str__()
        return rep


class WarDeck(war_karty.Deck):
    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.add(WarCard(rank, suit))


class WarPlayer(WarHand):
    def win(self):
        print(self.name, 'wygrał!')


class WarGame(object):
    def __init__(self, names):
        self.players = []
        self.round = {}
        self.scores = {}
        for name in names:
            player = WarPlayer(name)
            self.players.append(player)

        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()

    def __additional_deck(self):
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        if len(self.deck.cards) < 2:
            self.__additional_deck()

        print("Każdy gracz otrzymuje po jednej karcie.")
        self.deck.deal(self.players, per_hand=1)

        # pokazuje karty graczy i tworzy słownik {gracz: liczba punktów}
        for player in self.players:
            print("{player_card} : {card_value}".format(player_card=player, card_value=player.cards[0].value))
            self.scores[player] = player.cards[0].value

        # lista krotek posortowanych malejąco wg wyniku gracza: [(gracz, wynik)]
        sorted_scores = sorted(self.scores.items(), key=lambda s: s[1], reverse=True)
        print(sorted_scores)

        print([(k, self.scores[k]) for k in sorted(self.scores, key=self.scores.get, reverse=True)])

        # ogłasza wynik rundy
        print("Remis!") if sorted_scores[0][1] == sorted_scores[1][1] else \
            print("{} wygrał!".format(sorted_scores[0][0].name))

        for player in self.players:
            player.clear()


def main():
    print('\t\tWitaj w grze karcianej "Wojna"!\n')
    names = []
    number = war_gry.ask_number("Podaj liczbę graczy (2 - 4): ", low=2, high=4)
    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()
    game = WarGame(names)
    again = None
    while again != "n":
        game.play()
        again = war_gry.ask_yes_no("\nCzy chcesz zagrać ponownie? (t/n): \n")


main()
input('\n\nKoniec programu!')