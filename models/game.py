from deck import Deck

class Game(Deck):
    players_symbols = ("cp", "p1", "p2", "p3", "p4", "p5", "p6")
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
        self.hands = self.make_hand_dictionary()
        self.points = {}
        self.bet = 0

    def make_hand_dictionary(self):
        d = {}
        i = 0
        for p in self.players_symbols:
            d.setdefault(p, [])
            i += 1
            if i == self.players: break
        return d

    def first_deal(self):
        for c in range(2):
            for h in self.hands.keys():
                self.hands[h].append(self.get_card())

    def clear_hands(self):
        for k in self.hands.keys():
            self.hands[k] = []

    def get_hands(self):
        return self.hands

    def count_points(self):
        points_dict = self.make_hand_dictionary()
        for k, v in self.hands.items():
            points = 0
            for c in sorted(v):
                if c == "a":
                    if points > 10:
                        points += self.cards_values["aceLow"]
                    else:
                        points += self.cards_values["aceHigh"]
                else:
                    points += self.cards_values[c]
            points_dict[k] = points
        return points_dict