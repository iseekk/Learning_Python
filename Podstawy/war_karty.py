from random import shuffle

class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        return "{rank}{suit}".format(rank=self.rank, suit=self.suit) if self.is_face_up else "XX"

    @property
    def value(self):
        return self.RANKS.index(self.rank) + 1

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '<pusta>'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Nie mogę dalej rozdawać. Zabrakło kart!')

if __name__ == '__main__':
    print("To moduł zawierający klasy do gry w karty.")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")