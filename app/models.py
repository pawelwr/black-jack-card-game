from app import db
from random import shuffle


class Game(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    deck = db.Column(db.String)
    pc_cards = db.Column(db.String(20))
    p1_cards = db.Column(db.String(20))
    cards_values = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10,  'j': 10,
        'q': 10, 'k': 10,
        'aceLow': 1, 'aceHigh': 11
        }

    def __repr__(self):
        return '<Deck {}>'.format(self.deck)

    def shuffle_deck(self, number_of_decks=2):
        """
        Assumes: nothing
        Return: deck of shuffled cards
        TODO: for more than one deck
        """
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
        deck = []
        for i in range(number_of_decks * 4):
            for k in cards:
                deck.append(k)
                shuffle(deck)
        print('deck: ' + ",".join(deck))
        self.deck = ",".join(deck)

    def get_card(self):
        print("get_card deck: ", self.deck)
        cards = self.deck.split(',')
        card = cards.pop(0)
        self.deck = ",".join(cards)
        return card

    def user_get_card(self):
        card = self.get_card()
        print("card:", card)
        print("p1:", self.p1_cards)
        self.p1_cards += ',' + card

    def first_deal(self):
        self.pc_cards = ""
        self.p1_cards = ""
        cards = self.deck.split(",")
        print('cards: ' + str(cards))
        for c in range(2):
            self.pc_cards += cards.pop(0) + ','
            self.p1_cards += cards.pop(0) + ','
        self.p1_cards = self.p1_cards[:-1]
        self.pc_cards = self.pc_cards[:-1]
        self.deck = ",".join(cards)
        print('deck after join: ' + self.deck, 'p1_cards:', self.p1_cards)

    def get_hands(self):
        hands = {"pc": self.pc_cards, "p1": self.p1_cards}
        return hands

    def count_points(self, hand):
        points = 0
        cards = hand.split(',')
        for c in cards:
            if c == "": break
            if c == "a":
                if points > 10:
                    points += self.cards_values["aceLow"]
                else:
                    points += self.cards_values["aceHigh"]
            else:
                points += self.cards_values[c]
        return points
