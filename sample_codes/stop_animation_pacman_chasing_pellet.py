import tkinter as tk

class LoadingScreen:
    def __init__(self, canvas, calculated_reward_amount):
        self.calculated_reward_amount = calculated_reward_amount
        
        self.canvas = canvas
        self.canvas.title("Pacman Chasing Pellet")

        # Create Canvas
        self.canvas = tk.Canvas(canvas, width=500, height=200, bg="white")
        self.canvas.pack()

        # Initialize game elements
        self.pacman_open = True
        self.pacman = self.canvas.create_arc(50, 50, 100, 100, start=45, extent=270, fill="green", outline="yellow")
        self.pellet = self.canvas.create_oval(400, 75, 420, 95, fill="blue", outline="blue")

        # Start the animation
        self.move_pacman()

    def move_pacman(self):
        self.canvas.move(self.pacman, 15, 0)
        pacman_coords = self.canvas.coords(self.pacman)
        pellet_coords = self.canvas.coords(self.pellet)

        # Check collision with the pellet
        if pacman_coords[2] >= pellet_coords[0]:
            self.canvas.delete(self.pellet)
            self.canvas.create_text(250, 150, text='Bottle Processed! \n You have won {calculated_reward_amount}', font=("Arial", 14), fill="green")
            return

        # Toggle Pacman mouth
        if self.pacman_open:
            self.canvas.itemconfig(self.pacman, start=45, extent=270)
        else:
            self.canvas.itemconfig(self.pacman, start=0, extent=360)
        self.pacman_open = not self.pacman_open

        # Continue animation
        if pacman_coords[2] < 500:
            self.canvas.after(100, self.move_pacman)

# Create the main Tkinter window
if __name__ == "__main__":
    canvas = tk.Tk()
    game = LoadingScreen(canvas, calculated_reward_amount=10)
    canvas.mainloop()
