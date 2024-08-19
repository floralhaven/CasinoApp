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

class SlotMachine(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Slot Machine")
        self.geometry("2000x1000")  # Set the window size to 2000x1000

        # Create a canvas to place the background image
        self.canvas = tk.Canvas(self, width=2000, height=1000, bg="green")
        self.canvas.grid(row=0, column=0, columnspan=3, rowspan=2)

        # Load and resize the background image
        self.background_image = ImageTk.PhotoImage(
            Image.open(os.path.join(image_folder, "Slot Machine Barrel.png")).resize((1000, 500), Image.Resampling.LANCZOS)
        )
        # Place the background image on the canvas
        self.canvas.create_image(1000, 500, image=self.background_image, anchor=tk.CENTER)

        # Load and resize the reel images to 200x300
        self.images = [
            ImageTk.PhotoImage(Image.open(os.path.join(image_folder, file)).resize((200, 300), Image.Resampling.LANCZOS))
            for file in image_files
        ]

        # Create canvases for the reels
        self.reel1_canvas = tk.Canvas(self.canvas, width=200, height=265, bg="#FFD700", highlightthickness=0)
        self.reel1_image_id = self.reel1_canvas.create_image(100, 150)
        self.canvas.create_window(720, 565, anchor=tk.CENTER, window=self.reel1_canvas)
        
        self.reel2_canvas = tk.Canvas(self.canvas, width=200, height=265, bg="#FFD700", highlightthickness=0)
        self.reel2_image_id = self.reel2_canvas.create_image(100, 150)
        self.canvas.create_window(970, 565, anchor=tk.CENTER, window=self.reel2_canvas)
        
        self.reel3_canvas = tk.Canvas(self.canvas, width=200, height=265, bg="#FFD700", highlightthickness=0)
        self.reel3_image_id = self.reel3_canvas.create_image(100, 150)
        self.canvas.create_window(1205, 565, anchor=tk.CENTER, window=self.reel3_canvas)

        # Create a spin button on the canvas
        self.spin_button = tk.Button(self, text="Spin", font=("Helvetica", 14), command=self.spin_reels)
        self.spin_button_window = self.canvas.create_window(1000, 800, anchor=tk.CENTER, window=self.spin_button)

    def spin_reels(self):
        # Randomly select images for each reel
        self.reel1_canvas.itemconfig(self.reel1_image_id, image=random.choice(self.images))
        self.reel2_canvas.itemconfig(self.reel2_image_id, image=random.choice(self.images))
        self.reel3_canvas.itemconfig(self.reel3_image_id, image=random.choice(self.images))

        # Check if all three images match
        if (self.reel1_canvas.itemcget(self.reel1_image_id, "image") == 
            self.reel2_canvas.itemcget(self.reel2_image_id, "image") == 
            self.reel3_canvas.itemcget(self.reel3_image_id, "image")):
            self.show_result("You Won!")
        else:
            self.show_result("You Lost!")

    def show_result(self, result):
        # Display the result in a popup window
        result_window = tk.Toplevel(self)
        result_window.title("Result")
        result_window.geometry("300x100")  # Size for result window
        tk.Label(result_window, text=result, font=("Helvetica", 14)).pack(pady=10)
        tk.Button(result_window, text="OK", command=result_window.destroy, font=("Helvetica", 12)).pack(pady=10)

def start_game():
    SlotMachine().mainloop()

# If you want to run this file standalone, you can still use the following block:
if __name__ == "__main__":
    start_game()