import random
title=r"""

 _    _  ___  ______ 
| |  | |/ _ \ | ___ \
| |  | / /_\ \| |_/ /
| |/\| |  _  ||    / 
\  /\  / | | || |\ \ 
 \/  \/\_| |_/\_| \_|
                                                                
Note:Make sure your hand's value is higher than your oppenent
"""
print(title)
# Define the card ranks, suits, and values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Create a deck of cards
deck = [{'rank': rank, 'suit': suit, 'value': values[rank]} for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Divide the deck between two players
player1_hand = deck[:len(deck)//2]
player2_hand = deck[len(deck)//2:]

# Initialize scores
player1_score = 0
player2_score = 0

# Play the game
while len(player1_hand) > 0 and len(player2_hand) > 0:
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)

    print(f"Player 1: {card1['rank']} of {card1['suit']} vs. Player 2: {card2['rank']} of {card2['suit']}")

    if card1['value'] > card2['value']:
        print("Player 1 wins this round!")
        player1_score += 1
    elif card1['value'] < card2['value']:
        print("Player 2 wins this round!")
        player2_score += 1
    else:
        print("It's a tie! War!")

# Determine the winner
if player1_score > player2_score:
    print("Player 1 wins the game!")
elif player1_score < player2_score:
    print("Player 2 wins the game!")
else:
    print("It's a tie!")