from card_deck import *
from constants import *
import probabilities
import visualizer
import poker

def innitializeGame(NumberOfPlayers):
    deck = Deck()
    deck.shuffle()
    game = poker.PokerGame(NumberOfPlayers, deck)
    """
    card1, card2 = visualizer.requestHand(deck)
    game.setHand(game.getSelf(), deck.dealCARD(card1), deck.dealCARD(card2))
    visualizer.starting_table(game.players)"""
    game.setHand(game.getSelf(), deck.deal(), deck.deal())
    print(game.getSelf().getHand())
    probabilities.holeCards(game.getSelf().getHand())


if __name__ == "__main__":
    start, players = visualizer.welcome()
    if start:
        innitializeGame(players)
    else:
        quit()
