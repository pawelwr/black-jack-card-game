#TODO resize message format to console size

def welcome():
    print("Welcome to Black Jack game.\nEnter your username to play: ", sep = "")

def rules(self):
    #TODO print rules in game
    pass
def choose_user_decorator(self):
    #create new or load user
    pass

def incorrect_bet():
    print("Please type correct value of bet.\n(Numeric value which is lower than account balance.)")

def place_bet(cash):
    print("###################################")
    print("# Account status: {:<16}#".format(cash))
    print("###################################")
    print("Please place your bet: ", sep="")


def game_status(user, dealer, dealer_card_visibility): # TODO double possibility only after first dealing
    d_cards = ""
    u_cards = ""
    d_points = dealer.count_points()
    u_points = user.count_points()

    if dealer_card_visibility:
        for c in dealer.hand:
            d_cards += c + " "
    else:
        d_cards = dealer.hand[0] + " #"

    for c in user.hand:
        u_cards += c + " "

    print("###################################")
    if dealer_card_visibility:
        print("# Dealer cards: {:<8} pts: {:<4}#".format(d_cards, d_points))
    else:
        print("# Dealer cards: {:<18}#".format(d_cards))
    print("#                                 #")
    print("#                                 #")
    print("# bet: {:<27}#".format(user.bet))
    print("#                                 #")
    print("#                                 #")
    print("# Your cards: {:<9} pts: {:<5}#".format(u_cards, u_points))
    print("###################################")

def ask_about_user_decision_with_double(): # TODO double possibility only after first dealing
    print("Want to (h)it, (d)ouble or (s)tay?: ", sep = "")

def ask_about_user_decision(): # TODO double possibility only after first dealing
    print("Want to (h)it or (s)tay?: ", sep = "")

def bust():
    print("###################################")
    print("#             You bust!           #")
    print("###################################")

def won_hand():
    print("###################################")
    print("#             You won!            #")
    print("###################################")

def lost_hand():
    print("###################################")
    print("#             You lost!           #")
    print("###################################")

def draw():
    print("###################################")
    print("#               Draw!             #")
    print("#    You get your money back.     #")
    print("###################################")