import random
title = r"""
______                               _   
| ___ \                             | |  
| |_/ / __ _  ___ ___ __ _ _ __ __ _| |_ 
| ___ \/ _` |/ __/ __/ _` | '__/ _` | __|
| |_/ / (_| | (_| (_| (_| | | | (_| | |_ 
\____/ \__,_|\___\___\__,_|_|  \__,_|\__|
                                        
"""

print(title)
# Define card values
card_values = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 0,  # 10, Jack, Queen, and King have a value of 0 in Baccarat
    'Jack': 0,
    'Queen': 0,
    'King': 0
}

# Define the deck
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] * 4

# Function to calculate the hand value
def calculate_hand_value(hand):
    total_value = sum([card_values[card] for card in hand]) % 10
    return total_value

# Function to deal two cards
def deal_two_cards():
    return [deck.pop(random.randint(0, len(deck) - 1)), deck.pop(random.randint(0, len(deck) - 1))]

# Deal two cards to the player and two cards to the dealer
player_hand = deal_two_cards()
dealer_hand = deal_two_cards()

# Calculate and display the initial hands
player_value = calculate_hand_value(player_hand)
dealer_value = calculate_hand_value(dealer_hand)

print(f"Player's Hand: {', '.join(player_hand)} (Value: {player_value})")
print(f"Dealer's Hand: {', '.join(dealer_hand)} (Value: {dealer_value})")

# Determine the winner
if player_value > dealer_value:
    print("Player wins!")
elif player_value < dealer_value:
    print("Dealer wins!")
else:
    print("It's a tie!")

# Display the final hands
print(f"Final Player's Hand: {', '.join(player_hand)} (Value: {player_value})")
print(f"Final Dealer's Hand: {', '.join(dealer_hand)} (Value: {dealer_value})")
