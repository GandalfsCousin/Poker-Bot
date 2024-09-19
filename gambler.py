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

    def __str__(self):
        return (f"{constants.CARD_COLOURS[self.getHand()[0].getSuit()]}{self.getHand()[0]}"
                f"{constants.CARD_COLOURS[self.getHand()[1].getSuit()]}{self.getHand()[1]}\033[0m")


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

    def __str__(self):
        if self.folded:
            return f"{self.getHand()[0]}{self.getHand()[1]}"
        return f"|XX||XX|"

    def fold(self, card1: Card, card2: Card):
        self.folded = True
        self.hand = [card1, card2]

class Bot(Gambler):
    pass