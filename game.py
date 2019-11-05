import sys
import os

dirr = os.path.dirname(os.path.realpath(__file__))
dir_path = "{}/players".format(dirr)
sys.path.append(dir_path)

from shutil import get_terminal_size

import UI as ui
import player.players as players
from deck import Deck

def game():
    ui.welcome()
    username = input()

    user = players.User(username)
    user_decision = ""
    while user_decision != quit:
        dealer = players.Dealer()
        deck = Deck()
        while len(deck.deck) > 10 or user_decision != "n" or user.cash <= 0:
            dealer_cards_visibility = False
            ui.place_bet(user.get_cash())
            is_bet_correct = user.place_bet(user.get_cash())
            while not is_bet_correct:
                ui.incorrect_bet()
                is_bet_correct = user.place_bet(user.get_cash())

            user.clear_hand()
            dealer.clear_hand()

            first_dealing(user, dealer, deck)
            ui.game_status(user, dealer, dealer_cards_visibility)
            ui.ask_about_user_decision_with_double()
            user_input = input()
            user.user_decision(user_input, deck.get_card())

            while True:
                print(user.count_points())
                print("\n" * get_terminal_size().lines, end='')
                ui.game_status(user, dealer, dealer_cards_visibility)
                if user.count_points() > 20: break
                ui.ask_about_user_decision()
                user_input = input()
                user.user_decision(user_input, deck.get_card())

                if user_input == "s": break

            print("\n" * get_terminal_size().lines, end='')

            if user.count_points() > 21:
                ui.bust()
                continue

            dealer.dealer_turn(deck.get_card())
            dealer_cards_visibility = True
            ui.game_status(user, dealer, dealer_cards_visibility)
            if user.count_points() == dealer.count_points():
                ui.draw()
                user.cash += user.bet
            elif user.count_points() > dealer.count_points():
                ui.won_hand()
                user.cash += user.bet*2
            else:
                ui.lost_hand()


def first_dealing(user, dealer, deck):
    for i in range(2):
        user.add_card(deck.get_card())
        dealer.add_card(deck.get_card())
    #print("User cards: {}\nDealer cards: {})".format(user.hand, dealer.hand))

def choose_player(username):
    if players.User.is_user(username):
        #return loaded user
        pass
    else:
        user = players.User(username)
        return user
#clear terminal
# if platform.system()=="Windows":
#     subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine
# else: #Linux and Mac
#     print("\033c", end="")
game()
