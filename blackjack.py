import random

# Define card ranks, suits, and values
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Define functions to create a deck of cards and shuffle it
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

# Define a function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    ace_count = hand.count(('Ace', 'Hearts')) + hand.count(('Ace', 'Diamonds')) + hand.count(('Ace', 'Clubs')) + hand.count(('Ace', 'Spades'))
    
    for card in hand:
        rank = card[0]
        value += values[rank]
    
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    
    return value

# Define a function to display a player's hand
def display_hand(player_name, hand):
    print(f"{player_name}'s hand:")
    for card in hand:
        print(f"{card[0]} of {card[1]}")
    print(f"Total value: {calculate_hand_value(hand)}\n")

# Initialize the game
deck = create_deck()
shuffle_deck(deck)

player_hand = []
dealer_hand = []

# Deal initial cards
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# ASCII art title
title = r"""

______ _       ___  _____  _   __   ___  ___  _____  _   __
| ___ \ |     / _ \/  __ \| | / /  |_  |/ _ \/  __ \| | / /
| |_/ / |    / /_\ \ /  \/| |/ /     | / /_\ \ /  \/| |/ / 
| ___ \ |    |  _  | |    |    \     | |  _  | |    |    \ 
| |_/ / |____| | | | \__/\| |\  \/\__/ / | | | \__/\| |\  \
\____/\_____/\_| |_/\____/\_| \_/\____/\_| |_/\____/\_| \_/
                                                           
Note:Try to reach the number 21 as hand value.Do not cross 21.If the dealears hand values is above 21 or lower than your hand,you win otherwise you lose
"""

print(title)

# Main game loop
while True:
    # Display player's and dealer's hands
    display_hand("Player", player_hand)
    print(f"Dealer's face-up card:\n{dealer_hand[0][0]} of {dealer_hand[0][1]}\n")
    
    # Check for player blackjack or bust
    if calculate_hand_value(player_hand) == 21:
        print("Blackjack! Player wins!")
        break
    elif calculate_hand_value(player_hand) > 21:
        print("Player busts. Dealer wins.")
        break

    # Ask player to hit or stand
    action = input("Do you want to 'hit' or 'stand'? ").lower()
    
    if action == 'hit':
        player_hand.append(deck.pop())
    elif action == 'stand':
        # Dealer's turn
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
        
        # Display dealer's hand
        display_hand("Dealer", dealer_hand)
        
        # Determine the winner
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        
        if dealer_value > 21:
            print("Dealer busts. Player wins!")
        elif dealer_value > player_value:
            print("Dealer wins!")
        elif dealer_value < player_value:
            print("Player wins!")
        else:
            print("It's a tie!")
        
        break
    else:
        print("Invalid input. Please enter 'hit' or 'stand'.")

