from card_deck import *
from constants import *
import poker

deck = Deck()
deck.shuffle()

game = poker.PokerGame(3, deck)
game.setHand(game.getSelf(), deck.deal(), deck.deal())
print(game.players)
game.fold(game.players[1], Card(CARD_SUITS[1], CARD_RANKS[3]), Card(CARD_SUITS[3], CARD_RANKS[3]))
print(game.players)

