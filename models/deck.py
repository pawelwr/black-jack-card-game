from random import shuffle

class Deck:
    def __init__(self):
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
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
        return deck_of_cards

    def get_card(self):
        #giving card for player and removing from desk
        card = self.deck.pop(0)
        return card
