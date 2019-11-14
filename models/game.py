from deck import Deck

class Game(Deck):
    players_symbols = ("cp", "p1", "p2", "p3", "p4", "p5", "p6")

    def __init__(self, players = 2):
        Deck.__init__(self)
        self.players = players
        self.hands = self.make_hand_dictionary
        self.bet = 0

    def make_hand_dictionary(self):
        d = {}
        i = 0
        for p in players:
            d.setdefault(p, [])
            i += 1
            if i == self.players: break
        return d

    def first_deal(self, av_players = 2):
        players = ("cp", "p1", "p2", "p3")
        available_players = players[0:av_players]
        for i in available_players:
            for c in range(2):
                self.hands[i].append(self.get_card())

    def clear_hands(self):
        for k in self.hands.keys():
            self.hands[k] = []

    def get_hands(self):
        return self



    # def get card(self. player)
    #     pass
    # def bet to winer
    #     pass
    # def reset hands
    #     pass
    # def get game status
    #     pass
    # def count points
    #     pass
#     def compare points
# print(hand)
g = Game()
g.first_deal()
print(g.hands)
g.clear_hands()
print(g.hands)
g.first_deal()
print(g.hands)
