import tkinter as tk
from tkinter import ttk
import subprocess

# Create the main application window
app = tk.Tk()
app.title("Ganesan Casino")
app.configure(bg="blue")


# Set the screen size to 200x200 pixels
app.geometry("100x100")


# Create a function to launch the Pinochle.py script
def launch_pinochle():
    subprocess.run(["python", "blackjack.py"])

# Create a function to launch the GoFish.py script
def launch_gofish():
    subprocess.run(["python", "GoFish.py"])

# Create a function to launch the Slot Machine game
def launch_slotmachine():
    subprocess.run(["python", "slotmachine.py"])

# Create a function to launch the Roulette game
def launch_roulette():
    subprocess.run(["python", "roulette.py"])

# Create a function to launch the Craps game
def launch_craps():
    subprocess.run(["python", "craps.py"])

# Create a function to launch the Baccarat game
def launch_baccarat():
    subprocess.run(["python", "Baccarat.py"])  # Change "Baccarat.py" to the actual filename

# Create a function to launch the Keno game
def launch_keno():
    subprocess.run(["python", "keno.py"])

# Create a label for the combined text art
combined_text_art = """
 _____                                    
|  __ \                                   
| |  \/ __ _ _ __   ___  ___  __ _ _ __   
| | __ / _` | '_ \ / _ \/ __|/ _` | '_ \  
| |_\ \ (_| | | | |  __/\__ \ (_| | | | | 
 \____/\__,_|_| |_|\___||___/\__,_|_| |_| 
                                          
                                          
 _____           _                        
/  __ \         (_)                       
| /  \/ __ _ ___ _ _ __   ___             
| |    / _` / __| | '_ \ / _ \            
| \__/\ (_| \__ \ | | | | (_) |           
 \____/\__,_|___/_|_| |_|\___/            
                                          
"""

# Create a label for the combined text art
text_art_label = ttk.Label(app, text=combined_text_art)

# Configure the label's font and size
text_art_label.config(font=("Courier", 10))

# Pack the label
text_art_label.pack()

# Create a button to start the Blackjack game
pinochle_button = ttk.Button(app, text="Start Blackjack", command=launch_pinochle)
pinochle_button.pack(pady=10)

# Create a button to start the Go Fish game
gofish_button = ttk.Button(app, text="Start Go Fish", command=launch_gofish)
gofish_button.pack(pady=10)

# Create a button to start the Slot Machine game
slotmachine_button = ttk.Button(app, text="Start Slot Machine", command=launch_slotmachine)
slotmachine_button.pack(pady=10)

# Create a button to start the Roulette game
roulette_button = ttk.Button(app, text="Start Roulette", command=launch_roulette)
roulette_button.pack(pady=10)

# Create a button to start the Craps game
craps_button = ttk.Button(app, text="Start Craps", command=launch_craps)
craps_button.pack(pady=10)

# Create a button to start the Baccarat game
baccarat_button = ttk.Button(app, text="Start Baccarat", command=launch_baccarat)
baccarat_button.pack(pady=10)

# Create a button to start the Keno game
keno_button = ttk.Button(app, text="Start Keno", command=launch_keno)
keno_button.pack(pady=10)

# Create a function to launch the Red Dog game
def launch_reddog():
    subprocess.run(["python", "reddog.py"])

# Create a function to launch the Caribbean Poker game
def launch_caribbean_poker():
    subprocess.run(["python", "caribbeanpoker.py"])

# Create buttons for Red Dog and Caribbean Poker
reddog_button = ttk.Button(app, text="Start Red Dog", command=launch_reddog)
reddog_button.pack(pady=10)

caribbean_poker_button = ttk.Button(app, text="Start Texas Hold'them Poker", command=launch_caribbean_poker)
caribbean_poker_button.pack(pady=10)

# Create a function to launch the Caribbean Poker game
def launch_uno():
    subprocess.run(["python", "uno.py"])

# Create buttons for Red Dog and Caribbean Poker
uno_button = ttk.Button(app, text="Start UNO", command=launch_uno)
uno_button.pack(pady=10)

def launch_pinochle():
    subprocess.run(["python", "pinochle.py"])

# Create buttons for Red Dog and Caribbean Poker
pinochle_button = ttk.Button(app, text="Start Pinochle", command=launch_pinochle)
pinochle_button.pack(pady=10)

def launch_pinochle():
    subprocess.run(["python", "war.py"])

# Create buttons for Red Dog and Caribbean Poker
war_button = ttk.Button(app, text="Start War", command=launch_pinochle)
war_button.pack(pady=10)



