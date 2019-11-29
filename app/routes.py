from flask import render_template, url_for
from app import app
from app.models import Game


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/start_game')
def start_game():
    game = Game()
    game.first_deal()
    hands = game.get_hands()
    print(hands)
    p1_points = game.count_points(game.p1_cards)
    return render_template('start_game.html', deck=game.deck,
                    p1_cards=list(hands["p1"]), p1_points=p1_points)
