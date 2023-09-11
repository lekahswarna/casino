
import random
title=r"""

______ _____ _   _ _      _____ _____ _____ _____ 
| ___ \  _  | | | | |    |  ___|_   _|_   _|  ___|
| |_/ / | | | | | | |    | |__   | |   | | | |__  
|    /| | | | | | | |    |  __|  | |   | | |  __| 
| |\ \\ \_/ / |_| | |____| |___  | |   | | | |___ 
\_| \_|\___/ \___/\_____/\____/  \_/   \_/ \____/ 
                                                  
Note:Predict on which number out of 36 the ball will land on                                                 
"""
print(title)
# Define the pockets on the Roulette wheel
pockets = [
    "0",
    "32", "15", "19", "4", "21", "2", "25", "17", "34", "6", "27", "13", "36", "11", "30", "8", "23", "10", "5",
    "24", "16", "33", "1", "20", "14", "31", "9", "22", "18", "29", "7", "28", "12", "35", "3", "26"
]

# Function to spin the Roulette wheel and return a random pocket
def spin_wheel():
    return random.choice(pockets)

# Function to determine the color of a pocket
def pocket_color(pocket):
    if pocket == "0":
        return "green"
    elif pocket in ["32", "15", "19", "4", "21", "2", "25", "17", "34", "6", "27", "13", "36", "11", "30", "8", "23", "10", "5", "24", "16", "33", "1", "20", "14", "31", "9", "22", "18", "29", "7", "28", "12", "35", "3", "26"]:
        return "red"
    else:
        return "black"

# Function to display the result of a spin
def display_spin_result(result):
    color = pocket_color(result)
    print(f"The ball landed on {result}, which is {color}.")

# Main game loop
while True:
    print("\nWelcome to Roulette!")
    bet = input("Place your bet on a pocket (0-36) or type 'quit' to exit: ")

    if bet == 'quit':
        break

    if bet.isdigit() and 0 <= int(bet) <= 36:
        result = spin_wheel()
        display_spin_result(result)

        if bet == result:
            print("Congratulations! You won.")
        else:
            print("Sorry, you lost.")
    else:
        print("Invalid input. Please enter a number between 0 and 36 or 'quit' to exit.")

print("Thank you for playing Roulette!")
