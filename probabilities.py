from constants import *
from card_deck import *
from math import comb

def holeCards(hand: list[Card]):
    """
    :return: Probability distribution of each RANKING being best hand
    """
    probability = {"Royal Flush": 0.000032, "Straight Flush": 0.000279, "Four of a Kind": 0.00168, "Full House": 0.0260,
                   "Flush": 0.0303, "Straight": 0.0462, "Three of a Kind": 0.0483, "Two Pair": 0.235, "Pair": 0.438,
                   "High Card": 0.174}



    print(probability)