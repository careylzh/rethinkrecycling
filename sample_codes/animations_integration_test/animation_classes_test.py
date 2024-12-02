import tkinter as tk

class AnimationA:
    def __init__(self, canvas):
        self.canvas = canvas
        self.rect = None
        self.dx = 5  # Movement per frame
        self.running = False

    def start(self, callback):
        self.rect = self.canvas.create_rectangle(50, 50, 100, 100, fill="red")
        self.running = True
        self.callback = callback
        self.animate()

    def animate(self):
        if not self.running:
            return

        self.canvas.move(self.rect, self.dx, 0)
        x1, _, x2, _ = self.canvas.coords(self.rect)
        if x2 > 400:  # Stop condition
            self.running = False
            self.callback()  # Trigger next animation
        else:
            self.canvas.after(50, self.animate)

class AnimationB:
    def __init__(self, canvas):
        self.canvas = canvas
        self.oval = None
        self.dy = 5
        self.running = False

    def start(self, callback):
        self.oval = self.canvas.create_oval(200, 200, 250, 250, fill="blue")
        self.running = True
        self.callback = callback
        self.animate()

    def animate(self):
        if not self.running:
            return

        self.canvas.move(self.oval, 0, self.dy)
        _, y1, _, y2 = self.canvas.coords(self.oval)
        if y2 > 400:  # Stop condition
            self.running = False
            self.callback()  # Trigger next animation
        else:
            self.canvas.after(50, self.animate)

from itertools import cycle

class WinAnimation:
    def __init__(self, canvas, calculated_amount):
        self.canvas = canvas
        self.animation_circle = None
        # self.dy = 5
        self.running = False
        # self.configure(bg="white")
        self.calculated_amount = calculated_amount

    def start(self, callback):
        self.frames = cycle([(40, 40, 60, 60), (30, 30, 70, 70), (20, 20, 80, 80), (10, 10, 90, 90)])
        self.animation_circle = self.canvas.create_oval(10, 10, 90, 90, fill="green")
        self.running = True
        self.callback = callback
        self.animate()

    def animate(self):

        if not self.running:
            return

        # Start animation
        self.animate_loading()

        # _, y1, _, y2 = self.canvas.coords(self.oval)
        y2 = 401
        if y2 > 400:  # Stop condition
            self.running = False
            self.callback()  # Trigger next animation
        else:
            self.canvas.after(50, self.animate)


    def animate_loading(self):
        frame = next(self.frames)
        self.canvas.coords(self.animation_circle, *frame)
        self.canvas.after(200, self.animate_loading)  # Update every 200ms

class LoadingScreen:
    def __init__(self, canvas, calculated_amount):
        self.calculated_reward_amount = calculated_amount
        
        self.canvas = canvas
        self.pacman = None
        self.running = False
        # self.canvas.title("Pacman Chasing Pellet")

        # Create Canvas
        # self.canvas = tk.Canvas(canvas, width=500, height=200, bg="white")
        # self.canvas.pack()

        # # Start the animation
        # self.move_pacman()

    def start(self, callback):
        # Initialize game elements
        self.pacman_open = True
        self.pacman = self.canvas.create_arc(50, 50, 100, 100, start=45, extent=270, fill="green", outline="yellow")
        self.pellet = self.canvas.create_oval(400, 75, 420, 95, fill="blue", outline="blue")
        self.frames = cycle([(40, 40, 60, 60), (30, 30, 70, 70), (20, 20, 80, 80), (10, 10, 90, 90)])
        self.running = True
        self.callback = callback
        self.move_pacman()

    # def animate(self):
    #     if not self.running:
    #         return
    #     # Start animation
    #     # _, y1, _, y2 = self.canvas.coords(self.oval)
    #     y2 = 401
    #     if y2 > 400:  # Stop condition
    #         self.running = False
    #         self.callback()  # Trigger next animation
    #     else:
    #         self.canvas.after(50, self.animate)

    def move_pacman(self):
        self.canvas.move(self.pacman, 15, 0)
        pacman_coords = self.canvas.coords(self.pacman)
        pellet_coords = self.canvas.coords(self.pellet)

        # Check collision with the pellet
        try:
            if pacman_coords[2] >= pellet_coords[0]:
                self.canvas.delete(self.pellet)
                self.canvas.create_text(250, 150, text=f"Bottle Processed! \n You have won ${self.calculated_reward_amount}", font=("Arial", 14), fill="green")
                self.callback()
                return
        except IndexError:
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
# if __name__ == "__main__":
#     canvas = tk.Tk()
#     game = LoadingScreen(canvas, calculated_reward_amount=10)
#     canvas.mainloop()
