import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Use PIL (Pillow) to handle image formats

import BlackJack
import Poker
import Roulette
import SlotMachine
import Craps

BUTTON_SIZE = (200, 100)  # Size of the buttons

# Load images for buttons and background
def load_image(image_path, size=None):
    try:
        image = Image.open(image_path)
        if size:
            image = image.resize(size, Image.LANCZOS)  # Resize image to fit the button
        print(f"Loaded image {image_path} with size {image.size}")  # Debugging line
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
    messagebox.showinfo("Manage Money", "Money management will start here.")

def show_credits():
    messagebox.showinfo("Credits", "Credits information will be displayed here.")

def show_help():
    messagebox.showinfo("Help", "Help information will be displayed here.")

# Create the main menu window
def create_main_menu():
    main_window = tk.Tk()
    main_window.title("Casino Simulation")

    # Load images
    img_background = load_image("./Overall UI/Generic Felt Mat.jpeg", size=(main_window.winfo_screenwidth(), main_window.winfo_screenheight()))
    img_blackjack = load_image("./Overall UI/BlackJack Icon.png", size=BUTTON_SIZE)
    img_poker = load_image("./Overall UI/Poker Icon.png", size=BUTTON_SIZE)
    img_craps = load_image("./Overall UI/Craps Icon.png", size=BUTTON_SIZE)
    img_roulette = load_image("./Overall UI/Roulette Icon.png", size=BUTTON_SIZE)
    img_slots = load_image("./Overall UI/Slot Machine Icon.png", size=BUTTON_SIZE)

    if img_background:
        # Set background image
        background_label = tk.Label(main_window, image=img_background)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window
    else:
        print("Background image not loaded. Check file path and format.")

    # Create a title label
    title_label = tk.Label(main_window, text="Casino Simulation", font=("Arial", 24), bg='white')  # Adjust bg color if needed
    title_label.pack(pady=20)

    # Create buttons with images
    def create_button(img, command):
        return tk.Button(main_window, image=img, command=command, width=BUTTON_SIZE[0], height=BUTTON_SIZE[1], bg='white')

    if img_blackjack:
        btn_play_blackjack = create_button(img_blackjack, play_blackjack)
        btn_play_blackjack.image = img_blackjack  # Keep a reference to avoid garbage collection
        btn_play_blackjack.pack(pady=10)
    else:
        print("Blackjack image not loaded. Check file path and format.")

    if img_poker:
        btn_play_poker = create_button(img_poker, play_poker)
        btn_play_poker.image = img_poker
        btn_play_poker.pack(pady=10)
    else:
        print("Poker image not loaded. Check file path and format.")

    if img_craps:
        btn_play_craps = create_button(img_craps, play_craps)
        btn_play_craps.image = img_craps
        btn_play_craps.pack(pady=10)
    else:
        print("Craps image not loaded. Check file path and format.")

    if img_roulette:
        btn_play_roulette = create_button(img_roulette, play_roulette)
        btn_play_roulette.image = img_roulette
        btn_play_roulette.pack(pady=10)
    else:
        print("Roulette image not loaded. Check file path and format.")

    if img_slots:
        btn_play_slots = create_button(img_slots, play_slots)
        btn_play_slots.image = img_slots
        btn_play_slots.pack(pady=10)
    else:
        print("Slots image not loaded. Check file path and format.")

    btn_money = tk.Button(main_window, text="Manage Money", command=manage_money, width=20, bg='white')
    btn_money.pack(pady=10)

    btn_credits = tk.Button(main_window, text="Credits", command=show_credits, width=20, bg='white')
    btn_credits.pack(pady=10)

    btn_help = tk.Button(main_window, text="Help", command=show_help, width=20, bg='white')
    btn_help.pack(pady=10)

    main_window.mainloop()

# Start the application
if __name__ == "__main__":
    create_main_menu()
