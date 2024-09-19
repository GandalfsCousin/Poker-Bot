from card_deck import *
from constants import *
import poker

def innitializeGame():
    deck = Deck()
    deck.shuffle()
    game = poker.PokerGame(3, deck)
    game.setHand(game.getSelf(), deck.deal(), deck.deal())
    game.fold(game.players[1], Card(CARD_SUITS[1], CARD_RANKS[3]), Card(CARD_SUITS[3], CARD_RANKS[3]))



def welcome():
    print("#=========================================#\n"
          "║                POKER-BOT                ║\n"
          "║                ¯¯¯¯¯¯¯¯¯                ║\n"
          "║     taking the risk out of gambling     ║\n"
          "#=========================================#\n")


if __name__ == "__main__":
    welcome()
    innitializeGame()
