from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


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


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    cash = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    