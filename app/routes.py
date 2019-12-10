from flask import render_template, url_for
from app import app, db
from app.models import Game
from app.game_methods import GameMethods

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

    game = GameMethods()
    game.shuffle_deck()
    game.first_deal()
    db.session.add(game)
    db.session.commit()

    hands = game.get_hands()
    p1_points = game.count_points(hands["p1"])

    pc_cards_list = hands["pc"].split(',')
    pc_cards_invisible = [pc_cards_list[0], '#']

    return render_template(
        'game_table.html', deck=game.deck,
        p1_cards=hands["p1"].split(','), p1_points=p1_points,
        pc_cards=pc_cards_invisible)


@app.route('/get_card')
def get_card():
    game = GameMethods.query.get(1)
    game.user_get_card()
    db.session.add(game)
    db.session.commit()

    hands = game.get_hands()
    p1_points = game.count_points(hands["p1"])

    if p1_points > 21:
        pc_points = game.count_points(hands["pc"])
        return render_template(
            'bust.html', p1_cards=hands["p1"].split(','),
            p1_points=p1_points, pc_cards=hands["pc"].split(','),
            pc_points=pc_points
        )

    pc_cards_list = hands["pc"].split(',')
    pc_cards_invisible = [pc_cards_list[0], '#']

    return render_template(
                'game_table.html', deck=game.deck,
                p1_cards=hands["p1"].split(','), p1_points=p1_points,
                pc_cards=pc_cards_invisible
                )

@app.route('/stay')
def computer_turn():
    game = GameMethods.query.get(1)
    game.computer_turn()
    db.session.add(game)
    db.session.commit()

    hands = game.get_hands()
    p1_points = game.count_points(hands["p1"])
    pc_points = game.count_points(hands["pc"])

    if p1_points > pc_points or pc_points > 21:
        winner = "p1"
    elif p1_points == pc_points:
        winner = "draw"
    else:
        winner = "pc"

    messages = {"p1": "You win!", "draw": "Draw", "pc": "Computer win!"}

    return render_template(
        'game_table.html', deck=game.deck,
        p1_cards=hands["p1"].split(','), p1_points=p1_points,
        pc_cards=hands["pc"].split(','), pc_points=pc_points,
        message=messages[winner], show=True
        )

@app.route('/login')
def login():
    