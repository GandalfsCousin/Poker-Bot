import constants
import random


class Card():
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"|{self.suit[0]}{self.rank}|"

    def getValue(self):
        return constants.CARD_VALUES[self.rank]

    def getRank(self):
        return self.rank


class Deck():
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in constants.CARD_SUITS for rank in constants.CARD_RANKS]

    def shuffle(self):
        random.shuffle(self.deck)

    def getDeck(self):
        return self.deck
