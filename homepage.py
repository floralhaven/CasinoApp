from tkinter import ttk

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Welcome to the Game Application", font=("Arial", 24))
        label.pack(pady=10, padx=10)

        # Navigation buttons
        buttons = [
            ("BlackJack", "BlackJack"),
            ("Poker", "Poker"),
            ("Roulette", "Roulette"),
            ("SlotMachine", "Slotmachine"),
            ("Craps", "Craps"),
        ]

        for text, page_name in buttons:
            button = ttk.Button(self, text=text, command=lambda pn=page_name: controller.show_frame(pn))
            button.pack()
