
import random
title=r"""

 _____ _     _____ _____  ___  ___  ___  _____  _   _ _____ _   _  _____ 
/  ___| |   |  _  |_   _| |  \/  | / _ \/  __ \| | | |_   _| \ | ||  ___|
\ `--.| |   | | | | | |   | .  . |/ /_\ \ /  \/| |_| | | | |  \| || |__  
 `--. \ |   | | | | | |   | |\/| ||  _  | |    |  _  | | | | . ` ||  __| 
/\__/ / |___\ \_/ / | |   | |  | || | | | \__/\| | | |_| |_| |\  || |___ 
\____/\_____/\___/  \_/   \_|  |_/\_| |_/\____/\_| |_/\___/\_| \_/\____/ 
                                           
Note:Write 'enter' and let see if the sysmbols matches up before you run out of coins                           

"""
print(title)

# Define the symbols and their payouts
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]
payouts = {
    "Cherry": 2,
    "Lemon": 3,
    "Orange": 4,
    "Plum": 5,
    "Bell": 6,
    "Bar": 7,
    "Seven": 10
}

# Function to spin the slot machine
def spin_slot_machine():
    reels = [random.choice(symbols) for _ in range(3)]
    return reels

# Function to calculate the payout
def calculate_payout(reels):
    unique_symbols = set(reels)
    if len(unique_symbols) == 1:
        symbol = reels[0]
        return payouts[symbol]
    return 0

# Main game loop
balance = 10  # Starting balance
while balance > 0:
    input("Press Enter to spin the slot machine...")
    reels = spin_slot_machine()
    print("Reels:", reels)
    payout = calculate_payout(reels)
    if payout > 0:
        print(f"Congratulations! You won {payout} coins!")
        balance += payout
    else:
        print("Sorry, you didn't win this time.")
        balance -= 1  # Deduct one coin for each spin
    print(f"Your balance: {balance} coins\n")

print("Game over! You ran out of coins.")



    
   

    
   

    
   


      

     


        