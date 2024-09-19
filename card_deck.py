import constants
import random


class Card():
    """
    Class that handles Cards, 52 in deck
    """
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"|{self.suit[0]}{self.rank}|"

    def __eq__(self, other):
        if self.getSuit() == other.getSuit() and self.getRank() == other.getRank():
            return True
        return False

    def getValue(self):
        return constants.CARD_VALUES[self.rank]

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit


class Deck():
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in constants.CARD_SUITS for rank in constants.CARD_RANKS]

    def shuffle(self):
        random.shuffle(self.deck)

    def getDeck(self):
        return self.deck

    def deal(self):
        return self.deck.pop()

    def dealCARD(self, card: Card):
        return self.deck.pop(self.deck.index(card))

    def removeCard(self, cardToRemove: Card):
        self.deck.pop(self.deck.index(cardToRemove))
