import tkinter as tk
from tkinter import messagebox

def start_game():
    # Create a new Toplevel window
    root = tk.Toplevel()
    root.title("Craps Game")
    
    # Set the window size
    root.geometry("400x200")
    
    # Create a label to display "Coming Soon"
    coming_soon_label = tk.Label(root, text="Coming Soon", font=("Helvetica", 24, "bold"))
    coming_soon_label.pack(expand=True)

    # Optionally, you could add a button to close the window
    close_button = tk.Button(root, text="Close", command=root.destroy, font=("Helvetica", 14))
    close_button.pack(pady=20)
    
    # Start the main loop for this Toplevel window
    root.mainloop()

# Example usage
if __name__ == "__main__":
    start_game()
