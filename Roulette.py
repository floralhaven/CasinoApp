import tkinter as tk
import random
from PIL import Image, ImageTk  

color_map = {
    0: "Green",
    1: "Red", 2: "Black", 3: "Red", 4: "Black", 5: "Red", 6: "Black", 7: "Red", 8: "Black", 9: "Red", 10: "Black",
    11: "Black", 12: "Red", 13: "Black", 14: "Red", 15: "Black", 16: "Red", 17: "Black", 18: "Red", 19: "Red", 20: "Black",
    21: "Red", 22: "Black", 23: "Red", 24: "Black", 25: "Red", 26: "Black", 27: "Red", 28: "Black", 29: "Black", 30: "Red",
    31: "Black", 32: "Red", 33: "Black", 34: "Red", 35: "Black", 36: "Red"
}

class RouletteGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Roulette Game")
        self.geometry("400x450")
        
        # Load images
        self.roulette_image = ImageTk.PhotoImage(Image.open("Roulette/Roulette_SingleZero.png")) #
        self.red_image = ImageTk.PhotoImage(Image.open("Roulette/CircleRed.png"))
        self.black_image = ImageTk.PhotoImage(Image.open("Roulette/CircleBlack.png"))
        self.green_image = ImageTk.PhotoImage(Image.open("Roulette/CircleGreen.png"))
        
        # Roulette wheel display
        self.roulette_label = tk.Label(self, image=self.roulette_image)
        self.roulette_label.pack(pady=10)
        
        self.label = tk.Label(self, text="Place your bets!")
        self.label.pack(pady=10)
        
        self.number_label = tk.Label(self, text="Number (0-36):")
        self.number_label.pack()
        self.number_entry = tk.Entry(self)
        self.number_entry.pack(pady=5)
        
        self.color_label = tk.Label(self, text="Color (Red, Black, Green):")
        self.color_label.pack()
        self.color_entry = tk.Entry(self)
        self.color_entry.pack(pady=5)
        
        self.spin_button = tk.Button(self, text="Spin the Wheel!", command=self.spin_wheel)
        self.spin_button.pack(pady=10)
        
        self.result_image_label = tk.Label(self)  # Label to display result image
        self.result_image_label.pack(pady=10)
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

    def spin_wheel(self):
        try:
            number_bet = int(self.number_entry.get())
            color_bet = self.color_entry.get().capitalize()

            if number_bet < 0 or number_bet > 36 or color_bet not in ["Red", "Black", "Green"]:
                self.result_label.config(text="Invalid input. Please try again.", fg="red")
                return

            winning_number = random.randint(0, 36)
            winning_color = color_map[winning_number]

            result_text = f"The winning number is {winning_number} and the color is {winning_color}.\n"

            if number_bet == winning_number and color_bet == winning_color:
                result_text += "Congratulations! You've won on both number and color!"
            elif number_bet == winning_number:
                result_text += "Congratulations! You've won on the number!"
            elif color_bet == winning_color:
                result_text += "Congratulations! You've won on the color!"
            else:
                result_text += "Sorry, you didn't win this time."

            self.result_label.config(text=result_text, fg="green")
            
            # Display the corresponding color image
            if winning_color == "Red":
                self.result_image_label.config(image=self.red_image)
            elif winning_color == "Black":
                self.result_image_label.config(image=self.black_image)
            else:
                self.result_image_label.config(image=self.green_image)

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.", fg="red")

if __name__ == "__main__":
    game = RouletteGame()
    game.mainloop()
