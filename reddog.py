import random
title=r"""
______ _________________ _____ _____ 
| ___ \  ___|  _  \  _  \  _  |  __ \
| |_/ / |__ | | | | | | | | | | |  \/
|    /|  __|| | | | | | | | | | | __ 
| |\ \| |___| |/ /| |/ /\ \_/ / |_\ \
\_| \_\____/|___/ |___/  \___/ \____/
                                     
Note: Your third card should between card 1 and 2 to win                                    
"""
print(title)
# Define card ranks
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Function to shuffle and deal cards
def deal_cards():
    deck = [rank for rank in ranks for _ in range(4)]  # Create a deck with 4 of each rank
    random.shuffle(deck)  # Shuffle the deck
    return deck.pop(), deck.pop()  # Deal two initial cards

# Function to determine if a third card falls between the two initial cards
def is_third_card_between(card1, card2, third_card):
    card1_rank = ranks.index(card1)
    card2_rank = ranks.index(card2)
    third_card_rank = ranks.index(third_card)
    
    return card1_rank < third_card_rank < card2_rank or card2_rank < third_card_rank < card1_rank

# Main game loop
while True:
    input("Press Enter to deal two cards...")
    
    card1, card2 = deal_cards()
    print(f"Card 1: {card1}")
    print(f"Card 2: {card2}")
    
    third_card = random.choice(ranks)
    print(f"Third card: {third_card}")
    
    if is_third_card_between(card1, card2, third_card):
        print("You win!")
    else:
        print("You lose.")
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
