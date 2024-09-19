from card_deck import *

class Gambler():
    """
    Parent class for handling players and Bot, will contain main "playing" functions
    """
    def __init__(self):
        self.hand = []
        self.folded = False

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.getHand()}"

    def setHand(self, card1: Card, card2: Card):
        self.hand = [card1, card2]

    def getHand(self):
        return self.hand

    def fold(self, *args):
        self.folded = True



class Player(Gambler):
    def __repr__(self):
        if self.folded:
            return f"{self.__class__.__name__}: {self.getHand()}"
        return f"{self.__class__.__name__}: [|XX|, |XX|]"

    def fold(self, card1: Card, card2: Card):
        self.folded = True
        self.hand = [card1, card2]

class Bot(Gambler):
    pass