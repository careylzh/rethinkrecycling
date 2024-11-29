import tkinter as tk
from itertools import cycle

from sample_codes.expanding_heart import *

class LoseAnimation(tk.Tk):
    def __init__(self, calculated_amount):
        super().__init__()
        self.title("Lose Screen")
        self.geometry("500x200")
        self.configure(bg="white")
        self.resizable(False, False)
        self.calculated_amount = calculated_amount
        
        # Add a loading message
        self.label = tk.Label(
            self, 
            text=(f"Thank you for recycling Human, you have won my heart!\n Try again."), 
            font=("Arial", 14), 
            bg="green",
            fg="white"
        )
        self.label.pack(pady=20)
        
        # Add a canvas for the animation
        self.canvas = tk.Canvas(self, width=100, height=100, bg="white", highlightthickness=0)
        self.canvas.pack(pady=10)

        # Define heart frames
        # self.frames = cycle([
        #     self.calculate_heart_coordinates(scale) for scale in [1.0, 1.2, 1.5, 1.2]
        # ])
        # self.animation_heart = self.canvas.create_polygon(
        #     self.calculate_heart_coordinates(1.0), fill="red", outline="black"
        # )

        # Start animation
        # self.animate_loading()

    def destroy_screen(self):
        self.destroy()

    # def animate_loading(self):
    #     # Animate the heart by cycling through the frames
    #     frame = next(self.frames)
    #     self.canvas.coords(self.animation_heart, *frame)
    #     self.after(200, self.animate_loading)  # Update every 200ms
    #     self.after(500, )


# Uncomment to run the application
if __name__ == "__main__":
    app = LoseAnimation(calculated_amount=0)   
    app.mainloop()
