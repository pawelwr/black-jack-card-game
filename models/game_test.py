import pytest

from game import Game

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

def test_count_points():
    game = Game()
    game.hands = {"cp": ["a", "a"], "p1": ["a", "10"]}
    game.count_points()
    assert game.points == {"cp": 12, "p1": 21}

    game.hands = {"cp": ["2", "10", "a"], "p1": ["a", "a", "a"]}
    game.count_points()
    assert game.points == {"cp": 13, "p1": 13}

def test_computer_turn():
    game = Game()
    game.first_deal()
    game.computer_turn()
    del game.hands["cp"][-1]
    assert int(game.points["cp"]) > 17
