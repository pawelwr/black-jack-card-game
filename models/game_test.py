import pytest

from game import Game

def test_initial_empty_hands():
    game = Game()
    assert game.hands == {"cp": [], "p1": []}
    game = Game(3)
    assert game.hands == {"cp": [], "p1": [], "p2": []}
    game = Game(4)
    assert game.hands == {"cp": [], "p1": [], "p2": [], "p3": []}
    game = Game(5)
    assert game.hands == {"cp": [], "p1": [], "p2": [], "p3": [], "p4": []}
    game = Game(6)
    assert game.hands == {"cp": [], "p1": [], "p2": [], "p3": [], "p4": [], "p5": []}
    game = Game(7)
    assert game.hands == {"cp": [], "p1": [], "p2": [], "p3": [], "p4": [], "p5": [], "p6": []}

def test_first_deal():

    game = Game()
    game.first_deal()
    for h in game.hands.values():
        assert len(h) == 2

    game = Game(4)
    game.first_deal()
    for h in game.hands.values():
        assert len(h) == 2

    game = Game(7)
    game.first_deal()
    for h in game.hands.values():
        assert len(h) == 2

def test_clear_hands():

    game = Game()
    game.first_deal()
    game.clear_hands()
    for h in game.hands.values():
        assert len(h) == 0

    game = Game(4)
    game.first_deal()
    game.clear_hands()
    for h in game.hands.values():
        assert len(h) == 0

    game = Game(7)
    game.first_deal()
    game.clear_hands()
    for h in game.hands.values():
        assert len(h) == 0