import random
title=r""" 
 _____ ______  ___  ______  _____ 
/  __ \| ___ \/ _ \ | ___ \/  ___|
| /  \/| |_/ / /_\ \| |_/ /\ `--. 
| |    |    /|  _  ||  __/  `--. \
| \__/\| |\ \| | | || |    /\__/ /
 \____/\_| \_\_| |_/\_|    \____/ 
Note:Roll the dice. Your  point is the number the dice had given you.                  
  """
print(title)
# Function to roll two dice
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

# Function to play a round of Craps
def play_craps():
    input("Press Enter to roll the dice...")
    total = roll_dice()
    print(f"You rolled a total of {total}.")

    if total in (7, 11):
        print("You win!")
    elif total in (2, 3, 12):
        print("You lose!")
    else:
        point = total
        print(f"Your point is now {point}.")
        while True:
            input("Press Enter to roll the dice again...")
            new_total = roll_dice()
            print(f"You rolled a total of {new_total}.")
            if new_total == point:
                print("You win!")
                break
            elif new_total == 7:
                print("You lose!")
                break

# Main game loop
while True:
    print("Welcome to Craps!")
    play_craps()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
