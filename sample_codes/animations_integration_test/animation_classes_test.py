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
