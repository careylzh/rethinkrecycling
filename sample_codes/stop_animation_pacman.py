import tkinter as tk
import math

def animate():
    global animation_running
    if animation_running:
        # Get current Pac-Man coordinates
        x1, y1, x2, y2 = canvas.coords(pacman)

        # Update Pac-Man position (move horizontally)
        new_x1 = x1 + 10 if x2 < 300 else 0  # Reset when it reaches the edge
        new_x2 = new_x1 + (x2 - x1)  # Keep the width constant

        canvas.coords(pacman, new_x1, y1, new_x2, y2)

        # Schedule the next frame
        root.after(100, animate)

def stop_animation():
    global animation_running
    animation_running = False  # Stops the animation loop

def create_pacman(x, y, size, color):
    """Create a Pac-Man shape using an arc and a pie slice."""
    angle_start = 45
    angle_extent = 270
    return canvas.create_arc(
        x, y, x + size, y + size,
        start=angle_start,
        extent=angle_extent,
        fill=color,
        outline=""
    )

# Initialize tkinter
root = tk.Tk()
root.title("Pac-Man Animation")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Create a green Pac-Man to animate
pacman = create_pacman(10, 50, 50, "green")

animation_running = True
animate()  # Start the animation

# Stop the animation after 3 seconds
root.after(3000, stop_animation)

root.mainloop()
