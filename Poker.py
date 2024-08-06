import tkinter as tk

def start_game():
    # Create a new Tkinter window for Blackjack
    poker_window = tk.Tk()
    poker_window.title("Blackjack")

    # Setup the Blackjack game UI here
    # Example: Adding a label for now
    label = tk.Label(poker_window, text="5-Card Poker Game", font=("Arial", 24))
    label.pack(pady=20)

    # Add additional Blackjack UI elements and logic here

    poker_window.mainloop()
