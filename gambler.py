from card_deck import *

class Gambler():
    """
    Parent class for handling players and Bot, will contain main "playing" functions
    """
    def __init__(self):
        self.hand = []

    def setHand(self, card1: Card, card2: Card):
        self.hand = [card1, card2]

    def getHand(self):
        return self.hand


class Player(Gambler):
    pass

class Bot(Gambler):
    pass