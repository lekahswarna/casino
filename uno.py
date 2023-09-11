title=r"""

 _   _   _   _   _____ 
| | | | | \ | | |  _  |
| | | | |  \| | | | | |
| | | | | . ` | | | | |
| |_| | | |\  | \ \_/ /
 \___/  \_| \_/  \___/ 
                                           
Note:Plat the card with the same colour or number if you do not have draw a card.You also have two draw 2 card if you get draw 2,if skip happens the card players oppent gets skipped or if reverse happen the order is reversed.The first person to finish their hand wins.
"""
print(title)
import random

# Define card colors and values
colors = ["Red", "Green", "Blue", "Yellow"]
values = [str(i) for i in range(1, 10)] + ["Skip", "Reverse", "Draw Two"]

# Create a deck of Uno cards
deck = [(color, value) for color in colors for value in values]

# Define special action cards
special_cards = ["Skip", "Reverse", "Draw Two"]

# Initialize player hands
player1_hand = []
player2_hand = []

# Function to shuffle and deal cards to players
def deal_cards():
    random.shuffle(deck)
    for _ in range(7):
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())

# Function to display a player's hand
def display_hand(player_hand):
    for i, card in enumerate(player_hand):
        print(f"{i + 1}: {card[0]} {card[1]}")

# Function to check if a card can be played
def can_play(card, top_card):
    return card[0] == top_card[0] or card[1] == top_card[1]

# Initialize the top card on the discard pile
top_card = random.choice(deck)
deck.remove(top_card)

# Game loop
current_player = 1
deal_cards()

while True:
    print("\nTop card on the discard pile:", top_card[0], top_card[1])
    if current_player == 1:
        print("\nPlayer 1's turn:")
        display_hand(player1_hand)
        valid_move = False
        while not valid_move:
            try:
                choice = int(input("Enter the number of the card to play or 0 to draw a card: "))
                if choice == 0:
                    player1_hand.append(deck.pop())
                elif can_play(player1_hand[choice - 1], top_card):
                    played_card = player1_hand.pop(choice - 1)
                    top_card = played_card
                    if played_card[1] in special_cards:
                        if played_card[1] == "Skip":
                            current_player = 2
                        elif played_card[1] == "Reverse":
                            if current_player == 1:
                                current_player = 2
                            else:
                                current_player = 1
                        elif played_card[1] == "Draw Two":
                            current_player = 2
                            player2_hand.append(deck.pop())
                            player2_hand.append(deck.pop())
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
        if len(player1_hand) == 0:
            print("Player 1 wins!")
            break
        current_player = 2
    else:
        print("\nPlayer 2's turn:")
        display_hand(player2_hand)
        valid_move = False
        while not valid_move:
            try:
                choice = int(input("Enter the number of the card to play or 0 to draw a card: "))
                if choice == 0:
                    player2_hand.append(deck.pop())
                elif can_play(player2_hand[choice - 1], top_card):
                    played_card = player2_hand.pop(choice - 1)
                    top_card = played_card
                    if played_card[1] in special_cards:
                        if played_card[1] == "Skip":
                            current_player = 1
                        elif played_card[1] == "Reverse":
                            if current_player == 1:
                                current_player = 2
                            else:
                                current_player = 1
                        elif played_card[1] == "Draw Two":
                            current_player = 1
                            player1_hand.append(deck.pop())
                            player1_hand.append(deck.pop())
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
        if len(player2_hand) == 0:
            print("Player 2 wins!")
            break
        current_player = 1
