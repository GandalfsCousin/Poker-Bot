from card_deck import *
from constants import *
import visualizer
import poker

def innitializeGame(NumberOfPlayers):
    deck = Deck()
    deck.shuffle()
    game = poker.PokerGame(NumberOfPlayers, deck)
    game.setHand(game.getSelf(), deck.deal(), deck.deal())
    visualizer.starting_table(game.players)
    #game.fold(game.players[1], Card(CARD_SUITS[1], CARD_RANKS[3]), Card(CARD_SUITS[3], CARD_RANKS[3]))


if __name__ == "__main__":
    start, players = visualizer.welcome()
    if start:
        innitializeGame(players)
    else:
        quit()
