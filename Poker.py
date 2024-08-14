import tkinter as tk
from PIL import Image, ImageTk
import random
from collections import Counter

# Define card suits and ranks
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']

def create_deck():
    return [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_hand(deck, num_cards=5):
    if len(deck) < num_cards:
        raise ValueError("Not enough cards in the deck to deal")
    return [deck.pop() for _ in range(num_cards)]

def evaluate_hand(hand):
    suits = [card['suit'] for card in hand]
    ranks = [card['rank'] for card in hand]
    
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)
    
    is_flush = len(suit_counts) == 1
    rank_values = [ranks.index(rank) for rank in ranks]
    is_straight = len(rank_counts) == 5 and (max(rank_values) - min(rank_values) == 4)
    is_royal_flush = is_flush and sorted(ranks) == ['10', 'J', 'K', 'Q', 'A']

    if is_royal_flush:
        return 'Royal Flush'
    elif is_straight and is_flush:
        return 'Straight Flush'
    elif 4 in rank_counts.values():
        return 'Four of a Kind'
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        return 'Full House'
    elif is_flush:
        return 'Flush'
    elif is_straight:
        return 'Straight'
    elif 3 in rank_counts.values():
        return 'Three of a Kind'
    elif list(rank_counts.values()).count(2) == 2:
        return 'Two Pair'
    elif 2 in rank_counts.values():
        return 'Pair'
    else:
        return 'High Card'

def calculate_payout(rank):
    payouts = {
        'Pair': 1,
        'Two Pair': 5,
        'Three of a Kind': 10,
        'Straight': 25,
        'Flush': 50,
        'Full House': 100,
        'Four of a Kind': 1000,
        'Straight Flush': 10000,
        'Royal Flush': 100000,
    }
    return payouts.get(rank, 0)

class PokerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("5-Card Poker")
        self.money = 100  # Starting money

        # Create canvas for background
        self.canvas = tk.Canvas(self.root, width=1200, height=600)
        self.canvas.pack(fill="both", expand=True)
        
        # Load background image
        self.background_image = Image.open('./Poker/PokerTable.png')
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.canvas, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        # Create widgets on the canvas
        self.create_widgets()
        self.new_game()

        # Update canvas background on window resize
        self.root.bind('<Configure>', self.on_resize)

    def create_widgets(self):
        # Create widgets
        self.card_labels = [tk.Label(self.canvas) for _ in range(5)]
        self.hold_buttons = [tk.Button(self.canvas, text=f"Hold {i+1}", command=lambda i=i: self.toggle_hold(i), font=('Helvetica', 14, 'bold')) for i in range(5)]
        self.draw_button = tk.Button(self.canvas, text="Draw", command=self.draw, font=('Helvetica', 14, 'bold'))
        self.withdraw_button = tk.Button(self.canvas, text="Withdraw", command=self.withdraw, font=('Helvetica', 14, 'bold'))
        self.status_label = tk.Label(self.canvas, text=f"Money: ${self.money}", font=('Helvetica', 14, 'bold'))

        # Add widgets to canvas
        for label in self.card_labels:
            label.place_forget()  # Hide initially
        for button in self.hold_buttons:
            button.place_forget()  # Hide initially
        self.draw_button.place_forget()  # Hide initially
        self.withdraw_button.place_forget()  # Hide initially
        self.status_label.place_forget()  # Hide initially

    def update_widget_positions(self):
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        # Resize background image to fit the canvas
        resized_background = self.background_image.resize((width, height), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(resized_background)
        self.background_label.config(image=self.background_photo)
        
        # Define proportional positions for card labels and hold buttons
        card_positions = [
            (width * 0.0205, height * 0.68),
            (width * 0.237, height * 0.68),
            (width * 0.453, height * 0.68),
            (width * 0.669, height * 0.68),
            (width * 0.886, height * 0.68)
        ]
        hold_positions = [
            (width * 0.035, height * 0.57),
            (width * 0.251, height * 0.57),
            (width * 0.47, height * 0.57),
            (width * 0.685, height * 0.57),
            (width * 0.90, height * 0.57)
        ]

        # Update positions of widgets (without resizing card images here)
        for i, (x, y) in enumerate(card_positions):
            if self.card_labels[i]:
                self.card_labels[i].place(x=x, y=y, anchor='nw')

        for i, (x, y) in enumerate(hold_positions):
            if self.hold_buttons[i]:
                self.hold_buttons[i].place(x=x, y=y, anchor='nw')

        # Ensure that all other widgets are correctly positioned
        self.draw_button.place(x=width * 0.05, y=height * 0.05, anchor='nw')
        self.withdraw_button.place(x=width * 0.05, y=height * 0.15, anchor='nw')
        self.status_label.place(x=width * 0.05, y=height * 0.25, anchor='nw')

    def on_resize(self, event):
        self.update_widget_positions()
        self.update_card_sizes()

    def update_card_sizes(self):
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        img_width = int(width * 0.09)  # Example proportion for width
        img_height = int(height * 0.25)  # Example proportion for height

        # Ensure sizes are positive and non-zero
        img_width = max(img_width, 1)
        img_height = max(img_height, 1)

        for i, card in enumerate(self.hand):
            card_name = f"card{card['suit']}{card['rank']}.png" if card else "cardJoker.png"
            card_path = f"./BlackJack/Cards/{card_name}"
            card_image = Image.open(card_path)
            card_image = card_image.resize((img_width, img_height), Image.LANCZOS)
            img = ImageTk.PhotoImage(card_image)
            self.card_labels[i].config(image=img)
            self.card_labels[i].image = img  # Keep a reference to avoid garbage collection

    def update_display(self):
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        img_width = int(width * 0.1)  # Example proportion for width
        img_height = int(height * 0.2)  # Example proportion for height

        # Ensure sizes are positive and non-zero
        img_width = max(img_width, 1)
        img_height = max(img_height, 1)

        for i, card in enumerate(self.hand):
            card_name = f"card{card['suit']}{card['rank']}.png" if card else "cardJoker.png"
            card_path = f"./BlackJack/Cards/{card_name}"
            card_image = Image.open(card_path)
            card_image = card_image.resize((img_width, img_height), Image.LANCZOS)
            img = ImageTk.PhotoImage(card_image)
            self.card_labels[i].config(image=img)
            self.card_labels[i].image = img  # Keep a reference to avoid garbage collection

    def new_game(self):
        # Reset deck and hands
        self.deck = create_deck()
        shuffle_deck(self.deck)
        self.hand = deal_hand(self.deck)
        self.hold = [False] * 5
        self.update_display()
        self.status_label.config(text=f"Money: ${self.money}")

    def toggle_hold(self, index):
        self.hold[index] = not self.hold[index]
        self.hold_buttons[index].config(text="Hold" if self.hold[index] else f"Hold {index+1}")

    def draw(self):
        if len(self.deck) < self.hold.count(False):
            self.status_label.config(text="Not enough cards to draw.")
            return

        new_hand = [self.hand[i] if self.hold[i] else self.deck.pop() for i in range(5)]
        self.hand = new_hand
        self.update_display()
        self.evaluate_and_payout()

    def evaluate_and_payout(self):
        rank = evaluate_hand(self.hand)
        payout = calculate_payout(rank)
        self.money += payout
        self.status_label.config(text=f"Hand: {rank}, Payout: ${payout}. Money: ${self.money}")

    def withdraw(self):
        self.status_label.config(text=f"Withdrew ${self.money}. Returning to main menu.")
        self.money = 0
        self.new_game()

def start_game():
    root = tk.Toplevel()
    PokerGame(root)
    root.mainloop()

if __name__ == "__main__":
    start_game()
