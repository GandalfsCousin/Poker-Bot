from card_deck import *
from gambler import *

class PokerGame():
    def __init__(self, numberOfPlayers: int, autoplay: bool, deck: Deck):
        self.numberOfPlayers = numberOfPlayers
        self.autoplay = autoplay
        self.deck = deck

    def setHand(self, gambler: Gambler, card1: Card, card2: Card):


