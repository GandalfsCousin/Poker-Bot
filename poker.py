from card_deck import *
from gambler import *

class PokerGame():
    def __init__(self, numberOfPlayers: int, deck: Deck):
        self.numberOfPlayers = numberOfPlayers
        self.deck = deck
        self.river = []
        # Mode where Bot plays for you, and you can only input the bets taken by other players
        self.players = [Bot()]
        for i in range(1, numberOfPlayers):
            self.players.append(Player())

    def setHand(self, gambler: Gambler, card1: Card, card2: Card):
        gambler.setHand(card1, card2)

    def getPlayers(self):
        return self.players

    def setRiver(self, card1: Card, card2: Card, card3: Card):
        self.river += [card1, card2, card3]

    def getSelf(self):
        """
        :return: The Gambler Object that you are "playing" Always first player
        """
        return self.getPlayers()[0]

    def fold(self, gambler: Gambler, card1: Card, card2: Card):
        gambler.fold(card1, card2)
        self.deck.removeCard(card1)
        self.deck.removeCard(card2)





