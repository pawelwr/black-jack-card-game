import os


class Player(object):
    def __init__(self):
        self.hand = []
        self.cards_values = {
            '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10,  'j': 10,
            'q': 10, 'k': 10,
            'aceLow': 1, 'aceHigh': 10
            }

    def add_card(self, card):
        self.hand.append(card)

    def hit(self):
        self.add_card()
        pass

    def clear_hand(self):
        self.hand = []

    def stand(self):
        pass

    def count_points(self): #TODO BY GET FUNCTION ?????
        points = 0
        for c in sorted(self.hand):
            if c == "a":
                if points > 11:
                    points += self.cards_values["aceLow"]
                else:
                    points += self.cards_values["aceHigh"]
            else:
                points += self.cards_values[c]
        return int(points)

    def compare_points(self): #TODO with gt> function
        pass

# p = Player()
# print(p.count_points())

class User(Player):
    def __init__(self, name, cash = 5000, played_hand = 0, won_hand = 0):
        self.name = name
        self.cash = cash
        self.played_hand = played_hand
        self.won_hand = won_hand
        self.bet = 0
        Player.__init__(self)

    def place_bet(self, cash):
        # check that bet is bigger than account_status
        bet = input()
        if not bet.isnumeric():
            return False
        elif int(bet) > cash:
            return False
        else:
            self.bet = int(bet)
            self.cash -= int(bet)
            return True

    def user_decision(self, user_input, card):
        if user_input == "h":
            self.add_card(card)
        elif user_input == "d" and len(self.hand) == 2:
            self.add_card(card)
            self.bet *= 2

    def save_user(self):
        pass

    def get_cash(self):
        return self.cash
    @classmethod
    def is_user(cls, username):
        filename = "{}.txt".format(username)
        return os.path.isfile(filename)

    def load_user(self):
        pass

    @classmethod
    def choose_player(cls, username):
        if cls.is_user(username):
            #return loaded user
            pass
        else:
            user = User(username)
            return user

# u = User("paw")
# print(u.cash)
# u.place_bet(500)
# print(u.cash)

class Dealer(Player):
    def dealer_turn(self, card):
        while self.count_points() < 17:
            self.add_card(card)
