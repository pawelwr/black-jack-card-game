from flask import render_template, url_for
from app import app, db
from app.models import Game


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/start_game')
def start_game():
    g = Game.query.all()
    for r in g:
        db.session.delete(r)
    db.session.commit()

    game = Game()
    game.shuffle_deck()
    game.first_deal()
    db.session.add(game)
    db.session.commit()
    hands = game.get_hands()
    p1_points = game.count_points(hands["p1"])
    return render_template(
        'start_game.html', deck=game.deck,
        p1_cards=hands["p1"].split(','), p1_points=p1_points)


@app.route('/get_card')
def get_card():
    game = Game.query.get(1)
    game.user_get_card()
    db.session.add(game)
    db.session.commit()

    hands = game.get_hands()
    p1_points = game.count_points(hands["p1"])
    return render_template(
        'start_game.html', deck=game.deck,
        p1_cards=hands["p1"].split(','), p1_points=p1_points)


@app.route('/stay')
def computer_turn():
    game = Game.query.get(1)
    print('pc cards: ', game.pc_cards)
    game.computer_turn()
    db.session.add(game)
    db.session.commit()
    hands = game.get_hands()
    p1_points = game.count_points(hands["p1"])
    pc_points = game.count_points(hands["pc"])
    return render_template(
        'computer_turn.html', p1_cards=hands["p1"].split(','),
        p1_points=p1_points, pc_cards=hands["pc"].split(','),
        pc_points=pc_points
    )
