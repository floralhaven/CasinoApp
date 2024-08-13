import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# Define the path to the images
image_folder = "Slots"

# List of image file names
image_files = [
    "Wheel - Banana.png",
    "Wheel - Bars.png",
    "Wheel - Bell.png",
    "Wheel - Cherry.png",
    "Wheel - Lemon.png",
    "Wheel - Melon.png",
    "Wheel - Orange.png",
    "Wheel - Plum.png",
    "Wheel - Seven.png"
]

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")

        # Load images
        self.images = [ImageTk.PhotoImage(Image.open(os.path.join(image_folder, file))) for file in image_files]

        # Create three labels to display the reels
        self.reel1 = tk.Label(self.root)
        self.reel1.grid(row=0, column=0)
        self.reel2 = tk.Label(self.root)
        self.reel2.grid(row=0, column=1)
        self.reel3 = tk.Label(self.root)
        self.reel3.grid(row=0, column=2)

        # Create a spin button
        self.spin_button = tk.Button(self.root, text="Spin", command=self.spin_reels)
        self.spin_button.grid(row=1, column=1)

    def spin_reels(self):
        # Randomly select images for each reel
        self.reel1.config(image=random.choice(self.images))
        self.reel2.config(image=random.choice(self.images))
        self.reel3.config(image=random.choice(self.images))

        # Check if all three images match
        if self.reel1.cget("image") == self.reel2.cget("image") == self.reel3.cget("image"):
            self.show_result("You Won!")
        else:
            self.show_result("You Lost!")

    def show_result(self, result):
        # Display the result in a popup window
        result_window = tk.Toplevel(self.root)
        result_window.title("Result")
        tk.Label(result_window, text=result).pack()
        tk.Button(result_window, text="OK", command=result_window.destroy).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachine(root)
    root.mainloop()
