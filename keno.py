import random
title=r"""
 _   __ _____ _   _ _____ 
| | / /|  ___| \ | |  _  |
| |/ / | |__ |  \| | | | |
|    \ |  __|| . ` | | | |
| |\  \| |___| |\  \ \_/ /
\_| \_/\____/\_| \_/\___/ 

Note:Pick ten numbers between 1 and 80 and see  if your numbers match the keno numbers.That will decide your wins.
"""
print(title)
# Constants
MAX_NUMBERS = 80
NUM_PICKS = 10
BET_AMOUNT = 1
WINNING_ODDS = {
    0: 0,
    1: 3,
    2: 15,
    3: 50,
    4: 150,
    5: 300,
    6: 750,
    7: 1000,
    8: 5000,
    9: 10000,
    10: 50000,
}

# Generate Keno numbers
keno_numbers = random.sample(range(1, MAX_NUMBERS + 1), NUM_PICKS)



# Get the player's picks
player_picks = []
for i in range(NUM_PICKS):
    while True:
        try:
            pick = int(input(f"Pick {i + 1}/{NUM_PICKS}: Enter a number between 1 and {MAX_NUMBERS}: "))
            if 1 <= pick <= MAX_NUMBERS and pick not in player_picks:
                player_picks.append(pick)
                break
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Determine the number of matching picks
matching_picks = set(player_picks).intersection(keno_numbers)
num_matches = len(matching_picks)

# Calculate the winnings based on the number of matching picks
winnings = WINNING_ODDS.get(num_matches, 0)

# Display the results
print("\nYour Picks:", player_picks)
print("Matching Numbers:", matching_picks)
# Print the Keno numbers
print("Keno Numbers:", keno_numbers)
print(f"You matched {num_matches} numbers.")
print(f"Winnings: ${winnings * BET_AMOUNT}") 