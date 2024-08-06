import random
import tkinter as tk
from PIL import Image, ImageTk

# Define card suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create a deck of cards
deck = [(rank, suit) for suit in suits for rank in ranks]

# Function to get the file name for a card image
def get_card_image_filename(card):
    rank, suit = card
    return f"{rank}_of_{suit}.png"

# Function to load an image
def load_image(filename):
    image = Image.open(filename)
    image = image.resize((100, 150), Image.ANTIALIAS)  # Resize image if necessary
    return ImageTk.PhotoImage(image)

# Tkinter setup
root = tk.Tk()
root.title("5-Card Poker")

# Display player cards
player_cards = []
player_labels = []

# Load card back image
card_back_image = load_image("card_back.png")

for i in range(5):
    card = deck.pop()
    player_cards.append(card)
    image_filename = get_card_image_filename(card)
    card_image = load_image(image_filename)
    label = tk.Label(root, image=card_image)
    label.image = card_image  # Keep a reference
    label.pack(side="left")
    player_labels.append(label)

# Function to deal new cards
def deal():
    global player_cards, player_labels, deck
    deck.extend(player_cards)
    player_cards = []
    for label in player_labels:
        label.destroy()
    player_labels.clear()
    
    random.shuffle(deck)
    for i in range(5):
        card = deck.pop()
        player_cards.append(card)
        image_filename = get_card_image_filename(card)
        card_image = load_image(image_filename)
        label = tk.Label(root, image=card_image)
        label.image = card_image  # Keep a reference
        label.pack(side="left")
        player_labels.append(label)

# Deal button
deal_button = tk.Button(root, text="Deal", command=deal)
deal_button.pack()

root.mainloop()