import random

class Card(object):
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def display_card(self):
        print self.suit
        print self.num
        return self

    def get_card_val(self):
        return {self.num, self.suit}


class Deck(object):
    def __init__(self, num_cards = 52):
        self.num_cards = num_cards
        self.deck = []

        for card in range(0, 52):
            my_card = {}
            self.deck.append(my_card)

    def shuffle(self):
        card_dict = []

        for i in range(0, 52):
            rand

    def deal(self):

    def reset_deck(self):

class Player(Card):

    def hand(self):
