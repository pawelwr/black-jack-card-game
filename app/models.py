from app import db
from random import shuffle


class Game(db.Model):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    id = db.Column(db.Integer, primary_key=True)
    deck = db.Column(db.String(32))
    pc_cards = ""
    p1_cards = ""
    cards_values = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10,  'j': 10,
        'q': 10, 'k': 10,
        'aceLow': 1, 'aceHigh': 11
        }

    def __init__(self):
        self.deck = self.shuffle_deck(self.cards, 2)

    def shuffle_deck(self, cards, number_of_decks):
        """
        Assumes: nothing
        Return: deck of shuffled cards
        TODO: for more than one deck
        """
        deck_of_cards = []
        for i in range(number_of_decks * 4):
            for k in cards:
                deck_of_cards.append(k)
                shuffle(deck_of_cards)
        deck = ",".join(deck_of_cards)
        return deck

    def first_deal(self):
        self.pc_cards = ""
        self.p1_cards = ""
        for c in range(2):
            self.pc_cards += self.deck[0]
            self.deck = self.deck[2:]
            self.p1_cards += self.deck[0]
            self.deck = self.deck[2:]

    def get_hands(self):
        hands = {"pc": self.pc_cards, "p1": self.p1_cards}
        return hands

    def count_points(self, hand):
        for c in hand:
            points = 0
            if c == ",": continue
            if c == "a":
                if points > 10:
                    points += self.cards_values["aceLow"]
                else:
                    points += self.cards_values["aceHigh"]
            else:
                points += self.cards_values[c]
        return points