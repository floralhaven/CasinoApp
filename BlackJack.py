import tkinter as tk
import random
from PIL import Image, ImageTk

class Blackjack(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Blackjack")
        self.config(bg="#174718")
        
        self.player_hand = []
        self.dealer_hand = []
        self.deck = []
        self.game_active = True
        self.player_card_images = []
        self.dealer_card_images = []

        # If you have a canvas or any other widget using self.root, change it to self
        # Example:
        # self.canvas = tk.Canvas(self.root, width=2000, height=1000)
        # Change to:
        self.canvas = tk.Canvas(self, width=2000, height=1000)

        # Rest of your setup code...
        
        # Frames for layout
        top_frame = tk.Frame(self, bg="#174718")
        top_frame.pack(side=tk.TOP, pady=10)

        game_frame = tk.Frame(self, bg="#174718")
        game_frame.pack(pady=20)

        bottom_frame = tk.Frame(self, bg="#174718")
        bottom_frame.pack(side=tk.BOTTOM, pady=10)

        # Status label to display the game status
        self.status_label = tk.Label(top_frame, text="Welcome to Blackjack!", font=("Courier New", 14), bg="#174718", fg="white")
        self.status_label.pack()

        # Frames for card images
        self.player_hand_frame = tk.Frame(game_frame, bg="#174718")
        self.player_hand_frame.pack(pady=5)

        self.dealer_hand_frame = tk.Frame(game_frame, bg="#174718")
        self.dealer_hand_frame.pack(pady=5)

        # Buttons for game controls
        hit_button = tk.Button(bottom_frame, text="Hit", font=("Courier New", 14), command=self.hit, bg="#217839", fg="white")
        hit_button.pack(side=tk.LEFT, padx=10)

        stand_button = tk.Button(bottom_frame, text="Stand", font=("Courier New", 14), command=self.stand, bg="#217839", fg="white")
        stand_button.pack(side=tk.LEFT, padx=10)

        restart_button = tk.Button(bottom_frame, text="Restart", font=("Courier New", 14), command=self.restart, bg="#217839", fg="white")
        restart_button.pack(side=tk.LEFT, padx=10)

        # Start the game
        self.start_game()

    # Load card images
    def load_image(self, filename, size=(100, 150)):
        path = f"./BlackJack/Cards/{filename}"
        image = Image.open(path)
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

    # Create a new shuffled deck
    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [(value, suit, f"card{suit}{value}.png") for suit in suits for value in values]
        random.shuffle(deck)
        return deck

    # Calculate the score of a hand
    def calculate_score(self, hand):
        score = 0
        ace_count = 0
        for card in hand:
            value = card[0]
            if value in ['J', 'Q', 'K']:
                score += 10
            elif value == 'A':
                score += 11
                ace_count += 1
            else:
                score += int(value)
        # Adjust for Aces
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score

    # Update the display to show card images instead of text
    def update_display(self):
        # Clear previous images
        for widget in self.player_hand_frame.winfo_children():
            widget.destroy()
        for widget in self.dealer_hand_frame.winfo_children():
            widget.destroy()
        
        # Reset image lists
        self.player_card_images = []
        self.dealer_card_images = []

        # Display player's hand images
        for card in self.player_hand:
            card_image = self.load_image(card[2], size=(100, 150))
            card_label = tk.Label(self.player_hand_frame, image=card_image, bg="#174718")
            card_label.pack(side=tk.LEFT, padx=5)
            self.player_card_images.append(card_image)

        # Display dealer's hand images
        for card in self.dealer_hand:
            card_image = self.load_image(card[2], size=(100, 150))
            card_label = tk.Label(self.dealer_hand_frame, image=card_image, bg="#174718")
            card_label.pack(side=tk.LEFT, padx=5)
            self.dealer_card_images.append(card_image)
        
        # Update the status label with the current scores
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)
        
        if self.game_active:
            self.status_label.config(text=f"Player Score: {player_score} | Dealer Score: {dealer_score}")
        else:
            self.status_label.config(text=f"Player Score: {player_score}, Dealer Score: {dealer_score}")

    # Start a new game
    def start_game(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_active = True
        
        # Deal initial two cards to player and dealer
        self.player_hand.append(self.deck.pop())
        self.dealer_hand.append(self.deck.pop())
        self.player_hand.append(self.deck.pop())
        self.dealer_hand.append(self.deck.pop())
        
        # Update the display
        self.update_display()
        
        # Check for initial blackjack
        if self.calculate_score(self.player_hand) == 21:
            self.game_active = False
            self.status_label.config(text="Blackjack! Player wins!")
            return
        
        # Check for dealer blackjack
        if self.calculate_score(self.dealer_hand) == 21:
            self.game_active = False
            self.status_label.config(text="Dealer has Blackjack. Dealer wins!")
            return

    # Player hits
    def hit(self):
        if not self.game_active:
            return
        
        # Deal a card to the player
        self.player_hand.append(self.deck.pop())
        
        # Update the display
        self.update_display()
        
        # Check if player busts
        if self.calculate_score(self.player_hand) > 21:
            self.game_active = False
            self.status_label.config(text="Player busts! Dealer wins!")
            return

    # Player stands
    def stand(self):
        if not self.game_active:
            return
        
        # Dealer's turn to hit until they reach 17 or higher
        while self.calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
        
        # Update the display
        self.update_display()
        
        # Determine winner
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)
        
        if dealer_score > 21:
            self.status_label.config(text=f"Dealer busts! Player wins!")
        elif player_score > dealer_score:
            self.status_label.config(text=f"Player wins!")
        elif player_score < dealer_score:
            self.status_label.config(text=f"Dealer wins!")
        else:
            self.status_label.config(text=f"It's a draw!")
        
        self.game_active = False

    # Restart the game
    def restart(self):
        self.start_game()

def start_game():
    Blackjack().mainloop()
