title=r"""

 _____ _____  ______ _____ _____ _   _ 
|  __ \  _  | |  ___|_   _/  ___| | | |
| |  \/ | | | | |_    | | \ `--.| |_| |
| | __| | | | |  _|   | |  `--. \  _  |
| |_\ \ \_/ / | |    _| |_/\__/ / | | |
 \____/\___/  \_|    \___/\____/\_| |_/
                                       
Note:Try to four of a kind by asking for ranks like ace other wise you have to draw a card.It is impossible to win at this
"""
print(title)
import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Function to deal initial hands to players
def deal_initial_hands():
    player1_hand = [deck.pop() for _ in range(5)]
    player2_hand = [deck.pop() for _ in range(5)]
    return player1_hand, player2_hand

# Function to check if a player has a book (four cards of the same rank)
def check_for_books(player_hand):
    ranks_count = {}
    for card in player_hand:
        rank = card['rank']
        ranks_count[rank] = ranks_count.get(rank, 0) + 1
    for rank, count in ranks_count.items():
        if count == 4:
            return True, rank
    return False, None

# Function to play a turn
def play_turn(player_hand, opponent_hand, rank_to_ask):
    if rank_to_ask not in [card['rank'] for card in player_hand]:
        print("Go Fish! You draw a card.")
        drawn_card = deck.pop()
        player_hand.append(drawn_card)
        return False, None
    else:
        opponent_cards = [card for card in opponent_hand if card['rank'] == rank_to_ask]
        player_hand.extend(opponent_cards)
        opponent_hand[:] = [card for card in opponent_hand if card['rank'] != rank_to_ask]
        return True, rank_to_ask

# Main game loop
player1_hand, player2_hand = deal_initial_hands()

while True:
    print("\nPlayer 1's Hand:", [card['rank'] for card in player1_hand])
    print("Player 2's Hand:", [card['rank'] for card in player2_hand])

    player1_books, player1_book_rank = check_for_books(player1_hand)
    player2_books, player2_book_rank = check_for_books(player2_hand)

    if player1_books:
        print("Player 1 has a book of", player1_book_rank)
        player1_hand[:] = [card for card in player1_hand if card['rank'] != player1_book_rank]

    if player2_books:
        print("Player 2 has a book of", player2_book_rank)
        player2_hand[:] = [card for card in player2_hand if card['rank'] != player2_book_rank]

    if not player1_hand and not player2_hand:
        print("The game is a tie!")
        break

    # Player 1's turn
    while True:
        rank_to_ask = input("Player 1, ask for a rank: ")
        if rank_to_ask in ranks:
            break
        else:
            print("Invalid rank. Try again.")

    success, rank_asked = play_turn(player1_hand, player2_hand, rank_to_ask)

    if not player1_hand:
        print("Player 1 is out of cards. Player 2 wins!")
        break

    if success:
        print(f"Player 1 asked for {rank_asked} from Player 2 and got it.")
    else:
        print("Player 1 asked for a card they don't have. Go Fish!")

    # Player 2's turn
    while True:
        rank_to_ask = random.choice(ranks)
        if rank_to_ask in ranks:
            break

    success, rank_asked = play_turn(player2_hand, player1_hand, rank_to_ask)

    if not player2_hand:
        print("Player 2 is out of cards. Player 1 wins!")
        break

    if success:
        print(f"Player 2 asked for {rank_asked} from Player 1 and got it.")
    else:
        print("Player 2 asked for a card they don't have. Go Fish!")

