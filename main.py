import tkinter as tk
from tkinter import ttk
from homepage import HomePage
from BlackJack import BlackJack
from Poker import Poker
from Craps import Craps
from SlotMachine import SlotMachine
from Roulette import Roulette


class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Game Application")
        self.geometry("800x600")

        # Create a container for all frames
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Dictionary to store the frames
        self.frames = {}

        # Add frames to the dictionary
        for F in (HomePage, BlackJack, Poker, Craps, SlotMachine, Roulette):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Place all frames in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the home page
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()