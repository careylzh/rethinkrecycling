#import tkinter as tk
try:
    import Tkinter as tk

except ImportError:  # Python 3.x present
    import tkinter as tk
from itertools import cycle

class WinAnimation(tk.Tk):
    def __init__(self, calculated_amount):
        super().__init__()
        self.title("Win Screen")
        self.geometry("500x200")
        self.configure(bg="white")
        self.resizable(False, False)
        self.calculated_amount = calculated_amount
        
        # Add a loading message
        self.label = tk.Label(
            self, 
            text= (f"Congratulations Human, you have won ${calculated_amount}"), 
            font=("Arial", 14), 
            bg="green"
        )
        self.label.pack(pady=20)
        
        # Add a canvas for the animation
        self.canvas = tk.Canvas(self, width=100, height=100, bg="white", highlightthickness=0)
        self.canvas.pack(pady=10)

        # Define the animation frames (circle positions)
        self.frames = cycle([(40, 40, 60, 60), (30, 30, 70, 70), (20, 20, 80, 80), (10, 10, 90, 90)])
        self.animation_circle = self.canvas.create_oval(10, 10, 90, 90, fill="green")

        # Start animation
        self.animate_loading()

    def animate_loading(self):
        frame = next(self.frames)
        self.canvas.coords(self.animation_circle, *frame)
        self.after(200, self.animate_loading)  # Update every 200ms

# Run the application
# if __name__ == "__main__":
#     app = WinAnimation(calculated_amount)
#     app.mainloop()

