"""
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the 
file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
def get_hands(hand):
    """
    hand: string of 10 poker cards. [rank][suit]
    First 5 belong to "player1". Second 5 to "player 2"
    Returns 2 lists of 5 cards each.
    """
    hand_list = hand.split()
    p1 = hand_list[:5]
    p2 = hand_list[5:]
    return p1, p2
    
def get_points(hand):
    """
    hand: list of 5 cards [rank][suit]
    Returns points, ranks
    points: int from 1 to 10, based on best poker play
    ranks: list of ordered cards in the sequence 23456789:;<=>
    """
    suits = [card[1] for card in hand]
    ranks = ''.join([card[0] for card in hand])
    # Change card TJQKA for :;<=> in order to rank the cards with ord()
    ranks = ranks.replace('T', ':').replace('J', ';').replace('Q', '<').replace('K', '=').replace('A', '>')
    ranks = sorted(ranks)
    # Check if ordered cards
    ranks_str = ''.join(ranks)
    ordered = True if ord(ranks[4]) - ord(ranks[0]) == 4  and len(set(ranks)) == 5 else False
    # Check Royal Flush
    if len(set(suits)) == 1 and ranks == list(':;<=>'):#'TJQK'
        return 10, ranks
    # Check Straight Flush 
    elif len(set(suits)) == 1 and ordered:
        return 9, ranks # Return highest card
    # Check Four of a kind
    elif ranks_str.count(ranks_str[0]) == 4 or ranks_str.count(ranks_str[1]) == 4:
        return 8, ranks # Return different card
    # Check Full House
    elif len(set(ranks)) == 2:
        return 7, ranks # Return sum of cards
    elif len(set(suits)) == 1:
        return 6, ranks # ranks is ok
    elif ordered:
        return 5, ranks # ranks is ok
    elif ranks_str.count(ranks_str[0]) == 3 or ranks_str.count(ranks_str[1]) == 3 \
        or ranks_str.count(ranks_str[2]) == 3:
        return 4, ranks
    elif len(set(ranks)) == 3:
        return 3, ranks
    elif len(set(ranks)) == 4:
        return 2, ranks
    else:
        return 1, ranks

def untie_points61(ranks_1, ranks_2):
    """
    ranks_1, ranks_2: lists with cards.
    Return hand with highest valued cards. '1' if 1, else '2'
    """
    # Compare highest ranked cards in decreasing order
    if ranks_1[4] > ranks_2[4]:
        return '1'
    elif ranks_1[4] < ranks_2[4]:
        return '2'
    elif ranks_1[3] > ranks_2[3]:
        return '1'
    elif ranks_1[3] < ranks_2[3]:
        return '2'
    elif ranks_1[2] > ranks_2[2]:
        return '1'
    elif ranks_1[2] < ranks_2[2]:
        return '2'
    elif ranks_1[1] > ranks_2[1]:
        return '1'
    elif ranks_1[1] < ranks_2[1]:
        return '2'
    elif ranks_1[0] > ranks_2[0]:
        return '1'
    else:
        return '2'

def count_cards3(ranks):
    """
    ranks: list with 2 pairs, ordered
    returns:
    highest_pair, lowest_pair, other_card
    """
    ranks_str = ''.join(ranks)
    if ranks_str.count(ranks_str[4]) == 2:
        # Last card is highest pair
        highest_pair =  ranks[4]
        if ranks_str.count(ranks_str[2]) == 2:
            # 3th card is lowest pair
            lowest_pair = ranks_str[2]
            other = ranks_str[0]
        else:
            # 1st card is lowest pair
            lowest_pair = ranks[0]
            other = ranks_str[2]
    else:
        # Last card is other
        other = ranks[4]
        highest_pair = ranks[3]
        lowest_pair = ranks[0]
    return highest_pair, lowest_pair, other

def untie_points3(ranks_1, ranks_2):
    """
    ranks_1, ranks_2: lists with chars of 5 cards, ordered, with 2 pairs.
    Returns '1' if player 1 wins, else '2'
    """
    highest_pair_1, lowest_pair_1, other_1 = count_cards3(ranks_1)
    highest_pair_2, lowest_pair_2, other_2 = count_cards3(ranks_2)
    if highest_pair_1 > highest_pair_2:
        return '1'
    elif highest_pair_1 < highest_pair_2:
        return '2'
    elif lowest_pair_1 > lowest_pair_2:
        return '1'
    elif lowest_pair_1 < lowest_pair_2:
        return '2'
    elif other_1 > other_2:
        return '1'
    else:
        return '2'
def get_pair(ranks):
    """
    ranks: list of 5 ranks with one double
    Returns the card that doubles
    """
    ranks_str = ''.join(ranks)
    if ranks_str.count(ranks_str[0]) == 2:
        return ranks_str[0]
    elif ranks_str.count(ranks_str[1]) == 2:
        return ranks_str[1]
    elif ranks_str.count(ranks_str[2]) == 2:
        return ranks_str[2]
    else:
        return ranks_str[3]



def untie_points2(ranks_1, ranks_2):
    """
    ranks_1, ranks_2: lists of 5 cards, with one pair
    """
    double_1 = get_pair(ranks_1)
    double_2 = get_pair(ranks_2)
    ranks_1 = list(set(ranks_1))
    ranks_1.remove(double_1)
    ranks_2 = list(set(ranks_2))
    ranks_2.remove(double_2)
    if double_1 > double_2:
        return '1'
    elif double_1 < double_2:
        return '2'
    # Double ties. Compare Highest common
    elif ranks_1[2] > ranks_2[2]:
        return '1'
    elif ranks_1[2] < ranks_2[2]:
        return '2'
    # Compare lowest cards
    elif ranks_1[1] > ranks_2[1]:
        return '1'
    elif ranks_1[1] < ranks_2[1]:
        return '2'
    elif ranks_1[0] > ranks_2[0]:
        return '1'
    else:
        return '2'
    
def untie(p1, p2):
    """
    p1, p2: lists of 5 poker cards [rank][suit]
    p1 and p2 have same points
    Returns winner based on greatest value of hands. '1' for p1, '2' for p2
    """
    points_1, ranks_1 = get_points(p1)
    points_2, ranks_2 = get_points(p2)
    ranks_1str = ''.join(ranks_1)
    ranks_2str = ''.join(ranks_2)
    if points_1 == 9:
        if ranks_1[4] > ranks_2[4]:
            return '1'
        else:
            return '2'
    elif points_1 == 8:
        if ranks_1str.count(ranks_1str[0]) == 4:
            # First card is the quad
            highest_1 = ranks_1str[0]
            lowest_1 = ranks_1str[4]
        else:
            # Last card is the quad
            highest_1 = ranks_1str[4]
            lowest_1 = ranks_1str[0]
        if ranks_2str.count(ranks_2str[0]) == 4:
            # First card is the quad
            highest_2 = ranks_2str[0]
            lowest_2 = ranks_2str[4]
        else:
            # Last card is the quad
            highest_2 = ranks_2str[4]
            lowest_2 = ranks_2str[0]
        if highest_1 > highest_2:
            return '1'
        elif highest_2 > highest_1:
            return '2'
        # Quads are equal, untie
        elif lowest_1 > lowest_2:
            return '1'
        else:
            return '2'
    elif points_1 == 7:
        ranks_1 = set(ranks_1)
        ranks_2 = set(ranks_2)
        if ranks_1str.count(ranks_1str[0]) == 3:
            # First card is the triple
            highest_1 = ranks_1str[0]
            lowest_1 = ranks_1str[4]
        else:
            # Last card is the triple
            highest_1 = ranks_1str[4]
            lowest_1 = ranks_1str[0]
        if ranks_2str.count(ranks_2str[0]) == 3:
            # First card is the triple
            highest_2 = ranks_2str[0]
            lowest_2 = ranks_2str[4]
        else:
            # Last card is the triple
            highest_2 = ranks_2str[4]
            lowest_2 = ranks_2str[0]
        if highest_1 > highest_2:
            return '1'
        elif highest_2 > highest_1:
            return '2'
        # Triples are equal, untie with doubles
        elif lowest_1 > lowest_2:
            return '1'
        else:
            return '2'
    elif points_1 == 6:
        # Compare highest ranked cards in decreasing order
        return untie_points61(ranks_1, ranks_2)
    elif points_1 == 5:
        # Compare only highest card
        if ranks_1[4] > ranks_2[4]:
            return '1'
        else:
            return '2'
    elif points_1 == 4:
        # Hand 1
        if ranks_1str.count(ranks_1str[0]) == 3:
            # First card is the triple
            triple_1 = ranks_1str[0]
            highest_1 = ranks_1str[4]
            lowest_1 = ranks_1str[3]
        elif ranks_1str.count(ranks_1str[1]) == 3:
            # 2nd card is the triple
            triple_1 = ranks_1str[1]
            highest_1 = ranks_1str[4]
            lowest_1 = ranks_1str[0]
        else:
            # 3th card is the triple
            triple_1 = ranks_1str[2]
            highest_1 = ranks_1str[1]
            lowest_1 = ranks_1str[0]
        # Hand 2
        if ranks_2str.count(ranks_2str[0]) == 3:
            # First card is the triple
            triple_2 = ranks_2str[0]
            highest_2 = ranks_2str[4]
            lowest_2 = ranks_2str[3]
        elif ranks_2str.count(ranks_2str[1]) == 3:
            # 2nd card is the triple
            triple_2 = ranks_2str[1]
            highest_2 = ranks_2str[4]
            lowest_2 = ranks_2str[0]
        else:
            # 3th card is the triple
            triple_2 = ranks_2str[2]
            highest_2 = ranks_2str[1]
            lowest_2 = ranks_2str[0]
        if triple_1 > triple_2:
            return '1'
        elif triple_1 < triple_2:
            return '2'
        # Tie of triples
        elif highest_1 > highest_2:
            return '1'
        elif highest_1 < highest_2:
            return '2'
        # Tie of highest
        elif lowest_1 > lowest_2:
            return '1'
        else:
            return '2'
    elif points_1 == 3:
        return untie_points3(ranks_1, ranks_2)
    elif points_1 == 2:
        return untie_points2(ranks_1, ranks_2)
    else:
        # Compare highest ranked cards in decreasing order
        return untie_points61(ranks_1, ranks_2)

def rank(p1, p2):
    """
    p1, p2: Lists of 5 cards [rank][suit]
    Returns the winner, '1' or '2' 
    """
    points_1, ranks_1 = get_points(p1)
    points_2, ranks_2 = get_points(p2)
    print('points 1:', points_1, 'Points 2:', points_2, end=' ')
    if points_1 > points_2:
        return '1'
    elif points_2 > points_1:
        return '2'
    # Equal points
    else:
        print('Tie', end= ' ')
        if points_1 == 10:
            print('10 points TIE!')
        return untie(p1, p2)

def get_winner(hand):
    """
    hand: string of 10 poker cards. [rank][suit]
    First 5 belong to "player1". Second 5 to "player 2"
    Returns the winner. '1' for player 1, '2' for player '2'
    """
    p1, p2 = get_hands(hand)
    return rank(p1, p2)

   
file = open('p054_poker.txt', 'r') 
points_1 = 0
points_2 = 0
for hand in file:
    print(hand[:29], end= ' ')
    winner = get_winner(hand)
    print('Winner: Player ', winner)
    if winner == '1':
        points_1 += 1
    elif winner == '2':
        points_2 += 1
    else:
        print('No points :(')
file.close()
print(points_1, points_2, points_1 + points_2) 