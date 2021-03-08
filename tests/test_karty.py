import Podstawy.karty as k
import pytest
from mock import Mock
from copy import deepcopy

RANKS = ["A", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "J", "Q", "K"]
SUITS = ["c", "d", "h", "s"]
CARDS = [[r, s] for s in SUITS for r in RANKS]


@pytest.fixture()
def mock_hand():
    return Mock(spec=k.Card)


def deck_with_indices(CARDS):
    c = deepcopy(CARDS)
    for num in range(len(c)):
        c[num].append(num)
    return c


@pytest.mark.parametrize("exp_rank,exp_suit,index", deck_with_indices(CARDS))
def test_populate_first_card(exp_rank, exp_suit, index):
    deck = k.Deck()
    deck.populate()
    assert deck.cards[index].rank == exp_rank
    assert deck.cards[index].suit == exp_suit
