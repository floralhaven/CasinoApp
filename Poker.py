import tkinter as tk
from PIL import Image, ImageTk
import random
from collections import Counter

# Define card suits and ranks
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']

# Function to create a new deck of cards
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
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        # Create the GUI elements
        self.card_labels = [tk.Label(self.root) for _ in range(5)]
        for i, label in enumerate(self.card_labels):
            label.grid(row=0, column=i, padx=10, pady=10)

        self.hold_buttons = [tk.Button(self.root, text=f"Hold {i+1}", command=lambda i=i: self.toggle_hold(i)) for i in range(5)]
        for i, button in enumerate(self.hold_buttons):
            button.grid(row=1, column=i, padx=5)

        self.draw_button = tk.Button(self.root, text="Draw", command=self.draw)
        self.draw_button.grid(row=2, column=0, columnspan=5, pady=10)

        self.status_label = tk.Label(self.root, text=f"Money: ${self.money}")
        self.status_label.grid(row=3, column=0, columnspan=5)

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=4, column=0, columnspan=5, pady=10)

    def new_game(self):
        # Reset deck and hands
        self.deck = create_deck()
        shuffle_deck(self.deck)
        self.hand = deal_hand(self.deck)
        self.hold = [False] * 5
        self.update_display()
        self.status_label.config(text=f"Money: ${self.money}")

    def update_display(self):
        for i, card in enumerate(self.hand):
            card_name = f"card{card['suit']}{card['rank']}.png" if card else "cardJoker.png"
            img = Image.open(f"./BlackJack/Cards/{card_name}")
            img = img.resize((100, 150), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.card_labels[i].config(image=img)
            self.card_labels[i].image = img

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
        # Logic for withdrawing and possibly returning to the main menu
        self.status_label.config(text=f"Withdrew ${self.money}. Returning to main menu.")
        self.money = 0
        self.new_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = PokerGame(root)
    root.mainloop()
