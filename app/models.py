from app import db


class Game(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    deck = db.Column(db.String)
    pc_cards = db.Column(db.String(20))
    p1_cards = db.Column(db.String(20))
    bet = db.Column(db.Integer)
    cards_values = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10,  'j': 10,
        'q': 10, 'k': 10,
        'aceLow': 1, 'aceHigh': 11
        }

    def __repr__(self):
        return '<Deck {}>'.format(self.deck)
