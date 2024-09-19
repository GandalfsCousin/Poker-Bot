CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
CARD_RANKS = [' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', ' J', ' Q', ' K', ' A']
CARD_SUITS = ["Spades", "Clubs", "Hearts", "Diamonds"]
CARD_COLOURS = {"Spades": "\033[94m", "Clubs": "\033[92m", "Hearts": "\033[91m", "Diamonds": "\033[93m"}

HAND_RANKINGS = ["Royal Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pair", "Pair", "High Card"]

"""
high card scores 2 -> ace :                                             1-13
pair scores pair 2 -> pair ace:                                         14-26
Two Pair scores: lowest 2 pair, 3 pair -> highest King pair, Ace pair:  29-51
Just combine Pair results
Thee of a kind three 2's -> 3 Aces:                                     52-64
Straight, highest card 2->ace                                           65-77
Flush determined by highest card, 2 -> ace:                             78-90
Full House: Highest 3 of a kind, 2-2-2 -> ace-ace-ace                   91-103    
Four of a kind: 2-2-2 -> ace-ace-ace                                    104-116
straight flush: high card 2-> ace                                       117-129
Royal flush                                                             130
"""