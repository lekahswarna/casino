title=r""""

 _____ _______   __  ___   _____   _   _ _____ _    ______   _ ________  ___
|_   _|  ___\ \ / / / _ \ /  ___| | | | |  _  | |   |  _  \ ( )  ___|  \/  |
  | | | |__  \ V / / /_\ \\ `--.  | |_| | | | | |   | | | | |/| |__ | .  . |
  | | |  __| /   \ |  _  | `--. \ |  _  | | | | |   | | | |   |  __|| |\/| |
  | | | |___/ /^\ \| | | |/\__/ / | | | \ \_/ / |___| |/ /    | |___| |  | |
  \_/ \____/\/   \/\_| |_/\____/  \_| |_/\___/\_____/___/     \____/\_|  |_/


Note:Designate a dealer with a rotating button.
Use "small blind" and "big blind" forced bets, starting with the player to the dealer's left.
Deal two private "hole cards" to each player.
Texas Hold'em has several betting rounds:
Pre-Flop: Players can fold, call (match the big blind), or raise.
The Flop: Three face-up "flop" cards are dealt in the center, followed by a betting round.
The Turn: A fourth face-up "turn" card is dealt, with another betting round.
The River: A fifth face-up "river" card is dealt, leading to the final betting round.                           
"""
print(title)
import random

# Initialize the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Initialize player hands and community cards
players = [[] for _ in range(5)]
community_cards = []

# Initialize player funds (chips)
player_funds = [1000 for _ in range(5)]

# Betting amounts
small_blind = 10
big_blind = 20

# Function to display a player's hand
def display_hand(player_num):
    print(f"Player {player_num + 1}'s hand:")
    for card in players[player_num]:
        print(f"{card['rank']} of {card['suit']}")
    print()

# Deal two private cards to each player
for _ in range(2):
    for player in players:
        player.append(deck.pop())

# Show initial hands
for i in range(5):
    display_hand(i)

# Pre-flop betting
current_player = 2  # Player to the left of the big blind
current_bet = big_blind

while True:
    print(f"Player {current_player + 1}'s turn:")
    print(f"Current bet: {current_bet}")
    
    action = input("Enter 'fold', 'call', or 'raise': ").lower()
    
    if action == 'fold':
        print(f"Player {current_player + 1} folds.")
        player_funds[current_player] -= current_bet
        break
    elif action == 'call':
        print(f"Player {current_player + 1} calls.")
        player_funds[current_player] -= current_bet
        break
    elif action == 'raise':
        raise_amount = int(input("Enter raise amount: "))
        if raise_amount >= current_bet * 2:
            print(f"Player {current_player + 1} raises by {raise_amount}.")
            current_bet += raise_amount
            player_funds[current_player] -= current_bet
            current_player = (current_player + 1) % 5
        else:
            print("Minimum raise is double the current bet.")
    else:
        print("Invalid input. Please enter 'fold', 'call', or 'raise'.")

# Flop (3 community cards)
for _ in range(3):
    community_cards.append(deck.pop())

# Show the flop
print("Flop:")
for card in community_cards:
    print(f"{card['rank']} of {card['suit']}")
print()

# Flop betting
current_player = 0  # Player to the left of the dealer

while True:
    print(f"Player {current_player + 1}'s turn:")
    print(f"Current bet: {current_bet}")
    
    action = input("Enter 'check', 'bet', or 'fold': ").lower()
    
    if action == 'check':
        print(f"Player {current_player + 1} checks.")
        current_player = (current_player + 1) % 5
    elif action == 'bet':
        bet_amount = int(input("Enter bet amount: "))
        if bet_amount >= current_bet:
            print(f"Player {current_player + 1} bets {bet_amount}.")
            current_bet = bet_amount
            player_funds[current_player] -= current_bet
            current_player = (current_player + 1) % 5
        else:
            print("Bet must be at least the current bet.")
    elif action == 'fold':
        print(f"Player {current_player + 1} folds.")
        player_funds[current_player] -= current_bet
        break
    else:
        print("Invalid input. Please enter 'check', 'bet', or 'fold'.")

# Turn (1 community card)
community_cards.append(deck.pop())

# Show the turn
print("Turn:")
for card in community_cards:
    print(f"{card['rank']} of {card['suit']}")
print()

# Turn betting (same as flop betting)
current_player = 0

while True:
    print(f"Player {current_player + 1}'s turn:")
    print(f"Current bet: {current_bet}")
    
    action = input("Enter 'check', 'bet', or 'fold': ").lower()
    
    if action == 'check':
        print(f"Player {current_player + 1} checks.")
        current_player = (current_player + 1) % 5
    elif action == 'bet':
        bet_amount = int(input("Enter bet amount: "))
        if bet_amount >= current_bet:
            print(f"Player {current_player + 1} bets {bet_amount}.")
            current_bet = bet_amount
            player_funds[current_player] -= current_bet
            current_player = (current_player + 1) % 5
        else:
            print("Bet must be at least the current bet.")
    elif action == 'fold':
        print(f"Player {current_player + 1} folds.")
        player_funds[current_player] -= current_bet
        break
    else:
        print("Invalid input. Please enter 'check', 'bet', or 'fold'.")

# River (1 community card)
community_cards.append(deck.pop())

# Show the river
print("River:")
for card in community_cards:
    print(f"{card['rank']} of {card['suit']}")
print()

# River betting (same as turn betting)
current_player = 0

while True:
    print(f"Player {current_player + 1}'s turn:")
    print(f"Current bet: {current_bet}")
    
    action = input("Enter 'check', 'bet', or 'fold': ").lower()
    
    if action == 'check':
        print(f"Player {current_player + 1} checks.")
        current_player = (current_player + 1) % 5
    elif action == 'bet':
        bet_amount = int(input("Enter bet amount: "))
        if bet_amount >= current_bet:
            print(f"Player {current_player + 1} bets {bet_amount}.")
            current_bet = bet_amount
            player_funds[current_player] -= current_bet
            current_player = (current_player + 1) % 5
        else:
            print("Bet must be at least the current bet.")
    elif action == 'fold':
        print(f"Player {current_player + 1} folds.")
        player_funds[current_player] -= current_bet
        break
    else:
        print("Invalid input. Please enter 'check', 'bet', or 'fold'.")

# Showdown and determine the winner
hand_ranks = [max(players[i], key=lambda x: ranks.index(x['rank'])) for i in range(5)]
best_hand = max(hand_ranks, key=lambda x: ranks.index(x['rank']))

winning_players = [i+1 for i, hand in enumerate(hand_ranks) if hand == best_hand]

# Display the winner(s)
print(f"Winner(s) with the best hand ({best_hand['rank']} of {best_hand['suit']}): Player {', '.join(map(str, winning_players))}!")

# Display player funds (chips) after the game
for i in range(5):
    print(f"Player {i + 1}'s remaining chips: {player_funds[i]}")
