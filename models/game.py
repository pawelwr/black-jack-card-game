import sqlite3

from deck import Deck

class Game(Deck):
    """
    cp = computer players
    p1 = human player
    """
    cards_values = {
            '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10,  'j': 10,
            'q': 10, 'k': 10,
            'aceLow': 1, 'aceHigh': 11
            }

    def __init__(self, players = 2):
        Deck.__init__(self)
        self.players = players
        self.hands = {"cp": [], "p1": []}
        self.points = {"cp": 0, "p1": 0}
        self.bet = 0

    def first_deal(self):
        for c in range(2):
            for h in self.hands.keys():
                self.hands[h].append(self.get_card())

    def clear_hands(self):
        for k in self.hands.keys():
            self.hands[k] = []

    def get_hands(self):
        return self.hands

    def get_game_state(self):
        return

    def count_points(self):
        for k, v in self.hands.items():
            points = 0
            for c in v:
                if c == "a":
                    if points > 10:
                        points += self.cards_values["aceLow"]
                    else:
                        points += self.cards_values["aceHigh"]
                else:
                    points += self.cards_values[c]
            self.points[k] = points

    def get_points(self):
        return self.points

    def add_card(self, player):
        self.hands[player].append(self.get_card())
        return self.hands[player]

    def computer_turn(self):
        while self.points["cp"] < 17:
            self.add_card("cp")
            self.count_points()

    def load_user(self, username):
        conn = sqlite3.connect('bj.db')
        c = conn.cursor()
        query = "SELECT FROM users WHERE username={}".format(username)
        try:
            c.execute(query)
        except:
            
            