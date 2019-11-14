import pytest

from deck import Deck

def test_initial_deck():
    deck = Deck()
    assert len(deck.deck) == 104

def test_get_card():
    deck = Deck()
    assert len(deck.get_card()) == 1
    assert len(deck.deck) == 103

