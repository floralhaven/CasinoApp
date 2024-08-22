import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Use PIL (Pillow) to handle image formats

import BlackJack
import Poker
import Roulette
import SlotMachine
import Craps

# Load images for buttons and background
def load_image(image_path, size=None):
    try:
        image = Image.open(image_path)
        if size:
            image = image.resize(size, Image.LANCZOS)  # Resize image to fit the button
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

# Define functions for button actions
def play_blackjack():
    BlackJack.start_game()  # Call the start function from BlackJack.py

def play_poker():
    Poker.start_game()  # Call the start function from Poker.py

def play_craps():
    Craps.start_game()  # Call the start function from Craps.py

def play_roulette():
    Roulette.start_game()  # Call the start function from Roulette.py

def play_slots():
    SlotMachine.start_game()  # Call the start function from SlotMachine.py

def manage_money():
    messagebox.showinfo("Manage Money", "Money management coming soon!")

def show_credits():
    messagebox.showinfo("Credits", "Credits coming soon!")

def show_help():
    messagebox.showinfo("Help", "Help information coming soon!")

# Create the main menu window
def create_main_menu():
    main_window = tk.Tk()
    main_window.title("Casino Simulation")

    # Load images
    img_background = load_image("./Overall UI/Generic Felt Mat.jpeg")
    img_blackjack = load_image("./Overall UI/BlackJack Icon.png", size=(200, 100))
    img_poker = load_image("./Overall UI/Poker Icon.png", size=(200, 100))
    img_craps = load_image("./Overall UI/Craps Icon.png", size=(200, 100))
    img_roulette = load_image("./Overall UI/Roulette Icon.png", size=(200, 100))
    img_slots = load_image("./Overall UI/Slot Machine Icon.png", size=(200, 100))
    img_title = load_image("./Overall UI/Casino Icon.png", size=(300, 150)) 

    if img_background:
        # Set background image
        background_label = tk.Label(main_window, image=img_background)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window
        main_window.bg_image = img_background  # Keep a reference to avoid garbage collection
    else:
        print("Background image not loaded. Check file path and format.")

    if img_title:
        # Create a title image label
        title_label = tk.Label(main_window, image=img_title, bg='green')
        title_label.grid(row=0, column=0, columnspan=5, pady=20)
        main_window.title_image = img_title  # Keep a reference to avoid garbage collection
    else:
        print("Title image not loaded. Check file path and format.")

    # Configure grid weights to center content
    main_window.grid_rowconfigure(1, weight=1)
    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_columnconfigure(1, weight=1)
    main_window.grid_columnconfigure(2, weight=1)
    main_window.grid_columnconfigure(3, weight=1)
    main_window.grid_columnconfigure(4, weight=1)

    # Create buttons with images
    def create_button(img, command):
        return tk.Button(main_window, image=img, command=command, width=200, height=100, bg='green', relief='flat')

    if img_blackjack:
        btn_play_blackjack = create_button(img_blackjack, play_blackjack)
        btn_play_blackjack.image = img_blackjack  # Keep a reference to avoid garbage collection
        btn_play_blackjack.grid(row=1, column=0, padx=10, pady=10)
    else:
        print("Blackjack image not loaded. Check file path and format.")

    if img_poker:
        btn_play_poker = create_button(img_poker, play_poker)
        btn_play_poker.image = img_poker
        btn_play_poker.grid(row=1, column=1, padx=10, pady=10)
    else:
        print("Poker image not loaded. Check file path and format.")

    if img_craps:
        btn_play_craps = create_button(img_craps, play_craps)
        btn_play_craps.image = img_craps
        btn_play_craps.grid(row=1, column=2, padx=10, pady=10)
    else:
        print("Craps image not loaded. Check file path and format.")

    if img_roulette:
        btn_play_roulette = create_button(img_roulette, play_roulette)
        btn_play_roulette.image = img_roulette
        btn_play_roulette.grid(row=1, column=3, padx=10, pady=10)
    else:
        print("Roulette image not loaded. Check file path and format.")

    if img_slots:
        btn_play_slots = create_button(img_slots, play_slots)
        btn_play_slots.image = img_slots
        btn_play_slots.grid(row=1, column=4, padx=10, pady=10)
    else:
        print("Slots image not loaded. Check file path and format.")

    # Add additional buttons in a separate row
    btn_money = tk.Button(main_window, text="Manage Money", command=manage_money, width=20, bg='green', fg='white', font=('Helvetica', 14, 'bold'))
    btn_money.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    btn_credits = tk.Button(main_window, text="Credits", command=show_credits, width=20, bg='green', fg='white', font=('Helvetica', 14, 'bold'))
    btn_credits.grid(row=2, column=2, padx=10, pady=10)

    btn_help = tk.Button(main_window, text="Help", command=show_help, width=20, bg='green', fg='white', font=('Helvetica', 14, 'bold'))  
    btn_help.grid(row=2, column=3, columnspan=2, padx=10, pady=10)

    main_window.mainloop()

# Start the application
if __name__ == "__main__":
    create_main_menu()
