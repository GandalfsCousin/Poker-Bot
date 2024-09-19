from constants import *
from card_deck import *

import itertools
from collections import Counter

# choose the best 5 of 5, 5 of 6, 5 of 7
# Given the cards in your hand (2) and on the table (3-5) what is the best combination that you have?
# Cards have ranks and then internal rank (Ace vs 8)


def evaluate_hand(cards):
    # Extract ranks and suits from the cards
    ranks = [card.rank for card in cards]
    suits = [card.suit for card in cards]
    
    # Sort ranks using CARD_RANKS order
    sorted_ranks = sorted(ranks, key=lambda x: CARD_RANKS.index(x))
    
    # Convert ranks to their numeric values
    rank_values = [CARD_VALUES[card.rank] for card in cards]
    rank_count = Counter(rank_values).most_common()
    
    # Check if flush (all suits are the same)
    is_flush = len(set(suits)) == 1
    
    # Check if straight (5 consecutive ranks using CARD_RANKS)
    sorted_rank_indices = [CARD_RANKS.index(rank) for rank in sorted_ranks]
    is_straight = sorted_rank_indices == list(range(min(sorted_rank_indices), max(sorted_rank_indices) + 1))
    
    # Special case for low Ace straight (A, 2, 3, 4, 5)
    if sorted_ranks == ['2', '3', '4', '5', 'A']:
        is_straight = True
    
    # Now use the sorted `rank_values` for the rest of the hand evaluation
    # Royal Flush check (10, J, Q, K, A of the same suit)
    if is_flush and sorted_ranks == ['10', 'J', 'Q', 'K', 'A']:
        return HAND_RANKINGS[0]  # "Royal Flush"
    
    # Straight Flush check
    if is_straight and is_flush:
        return HAND_RANKINGS[1]  # "Straight Flush"
    
    # Four of a Kind check
    if rank_count[0][1] == 4:
        return HAND_RANKINGS[2]  # "Four of a Kind"
    
    # Full House check
    if rank_count[0][1] == 3 and rank_count[1][1] == 2:
        return HAND_RANKINGS[3]  # "Full House"
    
    # Flush check
    if is_flush:
        return HAND_RANKINGS[4]  # "Flush"
    
    # Straight check
    if is_straight:
        return HAND_RANKINGS[5]  # "Straight"
    
    # Three of a Kind check
    if rank_count[0][1] == 3:
        return HAND_RANKINGS[6]  # "Three of a Kind"
    
    # Two Pair check
    if rank_count[0][1] == 2 and rank_count[1][1] == 2:
        return HAND_RANKINGS[7]  # "Two Pair"
    
    # Pair check
    if rank_count[0][1] == 2:
        return HAND_RANKINGS[8]  # "Pair"
    
    # High Card check
    return HAND_RANKINGS[9]  # "High Card"

def best_hand(player_hand, community_cards):
    all_cards = player_hand + community_cards
    best_hand_rank = HAND_RANKINGS[-1]  # Start with the worst hand, "High Card"
    
    # Check all combinations of 5 cards
    for combination in itertools.combinations(all_cards, 5):
        hand_rank = evaluate_hand(combination)
        if HAND_RANKINGS.index(hand_rank) < HAND_RANKINGS.index(best_hand_rank):
            best_hand_rank = hand_rank
    
    return best_hand_rank

# Example usage:
player_hand = [Card('Hearts', 'A'), Card('Hearts', 'K')]  # Ace of Hearts, King of Hearts
community_cards = [Card('Clubs', 'Q'), Card('Hearts', 'J'), Card('Hearts', '10')]  # Queen, Jack, Ten

deck = Deck()
deck.shuffle()

print("Best hand:", best_hand(player_hand, community_cards))