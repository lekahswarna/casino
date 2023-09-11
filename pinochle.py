title=r"""

______ _____ _   _ _____ _____  _   _  _      _____ 
| ___ \_   _| \ | |  _  /  __ \| | | || |    |  ___|
| |_/ / | | |  \| | | | | /  \/| |_| || |    | |__  
|  __/  | | | . ` | | | | |    |  _  || |    |  __| 
| |    _| |_| |\  \ \_/ / \__/\| | | || |____| |___ 
\_|    \___/\_| \_/\___/ \____/\_| |_/\_____/\____/ 
                                                  
Note:Pick the winning suit and  you will have to decide how much you believe that.                                                
"""
print(title)
import random

# Define card ranks and suits
ranks = ['9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create a deck of cards (48 cards for Pinochle)
deck = [(rank, suit) for rank in ranks for suit in suits] * 2

# Remove 2s through 8s
deck = [card for card in deck if card[0] not in ('2', '3', '4', '5', '6', '7', '8')]

# Shuffle the deck
random.shuffle(deck)

# Define players and partnerships
players = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
partnerships = {'Player 1': 'Player 3', 'Player 2': 'Player 4', 'Player 3': 'Player 1', 'Player 4': 'Player 2'}

# Function to deal cards to players
def deal_hands():
    hands = {player: [] for player in players}
    for _ in range(4):
        for player in players:
            hands[player].append(deck.pop())
    return hands

# Function to determine the highest bidder and trump suit
def determine_trump_bid(bids):
    highest_bidder = max(bids, key=lambda k: bids[k])
    trump_bid = bids[highest_bidder]
    trump_suit = trump_bid.split()[-1]
    return highest_bidder, trump_suit

# Function to play a trick and determine the winner
def play_trick(lead_player, hands, trump_suit):
    trick = {}
    for _ in range(4):
        current_player = players[players.index(lead_player):] + players[:players.index(lead_player)]
        current_card = hands[current_player[0]].pop()
        trick[current_player[0]] = current_card
        lead_player = current_player[0]

    # Determine the winner of the trick
    winning_card = max(trick.values(), key=lambda card: (ranks.index(card[0]), suits.index(card[1])))
    winner = [player for player, card in trick.items() if card == winning_card][0]
    return winner

# Function to calculate scores
def calculate_scores(bids, tricks, trump_suit):
    scores = {player: 0 for player in players}
    for player in players:
        if bids[player] == f"{tricks[player]} {trump_suit}":
            scores[player] += 10 + tricks[player] * 2
        else:
            scores[partnerships[player]] += tricks[player] * 2
    return scores

# Main game loop
def play_pinochle():
    hands = deal_hands()
    bids = {}
    tricks = {player: 0 for player in players}

    # Bidding phase (simplified)
    for player in players:
        bid = input(f"{player}, enter your bid (e.g., '30 hearts'): ")
        bids[player] = bid

    highest_bidder, trump_suit = determine_trump_bid(bids)

    # Trick-taking phase
    for _ in range(12):
        lead_player = highest_bidder
        winner = play_trick(lead_player, hands, trump_suit)
        tricks[winner] += 1
        lead_player = winner

    # Calculate and print scores
    scores = calculate_scores(bids, tricks, trump_suit)
    for player, score in scores.items():
        print(f"{player}: {score} points")

    # Determine the winner of the game
    winning_team = max(partnerships, key=lambda k: scores[k])
    print(f"{winning_team} and {partnerships[winning_team]} win the game!")

# Start the game
play_pinochle()
