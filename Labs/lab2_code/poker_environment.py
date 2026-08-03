import random
import numpy as np
from operator import itemgetter
from cards_and_stacks import *

"""
Generate the cards for two players and each player has 5 cards in its hand.
There are total 52 cards in the games, and one card CANNOT be in both hands.
"""
def generate_2hands(nn_card=5):
    deck_ =[rank_+suit_ for suit_ in list(Suits.keys()) for rank_ in list(Ranks.keys())] # Generating deck 
    cards_ = random.sample(deck_, nn_card*2) # Randomly taking 10 cards    
    return cards_[:nn_card], cards_[nn_card:] # 5 cards to each player


"""
The Score of the Hand is a list with 3 elements:
Type of the Hand,
the highest rank(corresponding to the type of the hand),
and the suit of the highest rank(corresponding to the type of the hand),

"""
def identify_hand(Hand_):

    # Get the type of Hand
    def evaluateHand(Hand_):
        count = 0
        for card_1 in Hand_:
            for card_2 in Hand_:
                if (card_1[0] == card_2[0]) and (card_1[1] != card_2[1]):
                    count += 1
        return count

    # Use the "count" to analyse hand
    count_ = evaluateHand(Hand_)

    sub1 = 0
    score = [' ', ' ', ' ']

    if count_ == 12:
        for card_1 in Hand_:
            for card_2 in Hand_:
                if (card_1[0] == card_2[0]) and (card_1[1] != card_2[1]):
                    sub1 += 1
            if sub1 == 3:
                score = ['4OfAKind', card_1[0], card_1[1]]
                break

    elif count_ == 8:
        for card_1 in Hand_:
            for card_2 in Hand_:
                if (card_1[0] == card_2[0]) and (card_1[1] != card_2[1]):
                    sub1 += 1
            if sub1 == 1:
                sub1 = 0
            if sub1 == 2:
                score = ['FullHouse', card_1[0], card_1[1]]
                break

    elif count_ == 6:
        for card_1 in Hand_:
            for card_2 in Hand_:
                if (card_1[0] == card_2[0]) and (card_1[1] != card_2[1]):
                    sub1 += 1
            if sub1 == 2:
                score = ['3OfAKind', card_1[0], card_1[1]]
                break

    elif count_ == 4:
        need_card_1 = ['', '']
        need_card_2 = ['', '']
        for card_1 in Hand_:
            for card_2 in Hand_:
                # card_1 keep the first hand card, card_1 use every card to compare the card_1
                if card_1[0] == card_2[0] and card_1[1] != card_2[1]:
                    if Suits[card_1[1]] > Suits[card_2[1]]:
                        if need_card_1 == ['', '']:
                            need_card_1 = card_1
                    else:
                        if need_card_1 == ['', '']:
                            need_card_1 = card_2
                if card_1[0] == card_2[0] and card_1[1] != card_2[1] \
                        and card_1[0] != need_card_1[0] and card_2[0] != need_card_1[0]:
                    if Suits[card_1[1]] > Suits[card_2[1]]:
                        if need_card_2 == ['', '']:
                            need_card_2 = card_1
                    else:
                        if need_card_2 == ['', '']:
                            need_card_2 = card_2
        if Ranks[need_card_1[0]] > Ranks[need_card_2[0]]:
            score = ['TwoPairs', need_card_1[0], need_card_1[1]]
        else:
            score = ['TwoPairs', need_card_2[0], need_card_2[1]]

    elif count_ == 2:
        for card_1 in Hand_:
            for card_2 in Hand_:
                if (card_1[0] == card_2[0]) and (card_1[1] > card_2[1]):
                    sub1 += 1
            if sub1 == 1:
                score = ['OnePair', card_1[0], card_1[1]]
                break

    elif count_ == 0:
        def sortHand(Hand_):
            hand_sorted_ = sorted([[card_, Ranks[card_[0]]] for card_ in Hand_], key=itemgetter(1))[:]
            return [card_[0] for card_ in hand_sorted_]

        Hand_ = sortHand(Hand_)
        score = ['HighCard', Hand_[4][0], Hand_[4][1]]

        if Hand_[0][1] == Hand_[1][1] == Hand_[2][1] == Hand_[3][1] == Hand_[4][1]:
            score = ['Flush', Hand_[4][0], Hand_[4][1]]

        if (Ranks[Hand_[4][0]] - Ranks[Hand_[3][0]] == 1) \
                and (Ranks[Hand_[3][0]] - Ranks[Hand_[2][0]] == 1) \
                and (Ranks[Hand_[2][0]] - Ranks[Hand_[1][0]] == 1) \
                and (Ranks[Hand_[1][0]] - Ranks[Hand_[0][0]] == 1):
            score = ['Straight', Hand_[4][0], Hand_[4][1]]

            if Hand_[0][1] == Hand_[1][1] == Hand_[2][1] == Hand_[3][1] == Hand_[4][1]:
                score = ['StraightFlush', Hand_[4][0], Hand_[4][1]]
    else:
        exit(5664)
    return score


def poker_strategy_example(opponent_hand, opponent_hand_rank, opponent_stack, agent_action, agent_action_value, agent_stack, current_pot, bidding_nr):

    OPPONENT_ACTION = None
    OPPONENT_ACTION_VALUE = None

    MAX_PHASE = 6

    # Computes the hand strength
    def compute_hand_strength(type_rank, hand_rank):
        return type_rank*13+hand_rank

    # Check Hand power
    def get_strength_interval(type_rank, hand_rank):
        strength = Types[type_rank]*13+Ranks[hand_rank]
        if strength <= 13: return 'weak'
        elif strength <= 13*3: return 'median'
        else: return 'strong'

    opponent_hand_strength = get_strength_interval(opponent_hand, opponent_hand_rank)

    if bidding_nr >= MAX_PHASE:
        OPPONENT_ACTION = 'CALL'
        OPPONENT_ACTION_VALUE = 5

    elif opponent_stack >= 25:

        if opponent_hand_strength == 'weak':
            if bidding_nr < 3:
                if agent_action_value == 25:
                    OPPONENT_ACTION = 'BET'
                    OPPONENT_ACTION_VALUE = 10
                else:
                    OPPONENT_ACTION = 'BET'
                    OPPONENT_ACTION_VALUE = [10, 25][np.random.randint(2)]

            elif bidding_nr >= 3:
                if agent_action_value == 25:
                    OPPONENT_ACTION = 'FOLD'
                    OPPONENT_ACTION_VALUE = 0
                else:
                    OPPONENT_ACTION = 'CALL'
                    OPPONENT_ACTION_VALUE = 25

        elif opponent_hand_strength == 'median':
            if bidding_nr < 2:
                if agent_action_value == 25:
                    OPPONENT_ACTION = 'BET'
                    OPPONENT_ACTION_VALUE = 10
                else:
                    OPPONENT_ACTION = 'BET'
                    OPPONENT_ACTION_VALUE = 25

            elif bidding_nr >= 2:
                if agent_action_value == 25:
                    OPPONENT_ACTION = 'BET'
                    OPPONENT_ACTION_VALUE = 25
                else:
                    OPPONENT_ACTION = 'CALL'
                    OPPONENT_ACTION_VALUE = 5

        elif opponent_hand_strength == 'strong':
            if bidding_nr < 2:
                if agent_action_value == 25:
                    OPPONENT_ACTION = 'BET'
                    OPPONENT_ACTION_VALUE = 25
                else:
                    OPPONENT_ACTION = 'BET'
                    OPPONENT_ACTION_VALUE = 10

            elif bidding_nr >= 2:
                if agent_action_value == 25:
                    OPPONENT_ACTION = 'BET'
                    OPPONENT_ACTION_VALUE = 25
                else:
                    OPPONENT_ACTION = 'CALL'
                    OPPONENT_ACTION_VALUE = 5

    else:
        OPPONENT_ACTION = 'CALL'
        OPPONENT_ACTION_VALUE = 5

    return OPPONENT_ACTION, OPPONENT_ACTION_VALUE
