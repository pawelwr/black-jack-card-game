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

def test_count_points():
    game = Game()
    game.hands = {"cp": ["a", "a"], "p1": ["a", "10"]}
    assert game.count_points() == {"cp": 12, "p1": 21}

    game.hands = {"cp": ["2", "10", "a"], "p1": ["a", "a", "a"]}
    assert game.count_points() == {"cp": 13, "p1": 13}

    game.hands = {"cp": ["a", "a"], "p1": ["a", "10"], "p2": ["4", "6", "10", "a"]}
    assert game.count_points() == {"cp": 12, "p1": 21, "p2" : 21}

    game.hands = {"cp": ["a", "a"], "p1": ["a", "10"],
                "p2": ["4", "6", "10", "a"], "p3" : ["2", "10", "10"],
                "p4": ["7", "7", "a", "10", "2"], "p5": ["a", "a", "10"], "p6": ["2"]}
    assert game.count_points() == {"cp": 12, "p1": 21, "p2": 21, "p3": 22, "p4": 27, "p5": 22, "p6": 2 }
