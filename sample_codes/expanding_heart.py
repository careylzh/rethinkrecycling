import tkinter as tk
import math

def draw_heart(canvas, scale, color="green"):
    # Draw a heart on the canvas with the given scale.
    canvas.delete("heart")  # Clear the previous heart
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    center_x = width // 2
    center_y = height // 2

    points = []
    for t in range(0, 360, 1):
        t_rad = math.radians(t)
        x = 16 * math.sin(t_rad)**3
        y = 13 * math.cos(t_rad) - 5 * math.cos(2 * t_rad) - 2 * math.cos(3 * t_rad) - math.cos(4 * t_rad)
        points.append((center_x + x * scale, center_y - y * scale))

    for i in range(len(points) - 1):
        canvas.create_line(points[i], points[i + 1], fill=color, tags="heart", width=2)

def animate_heart(canvas):
    # Animate the expanding heart.
    scale = 1  # Initial scale
    max_scale = 15  # Maximum scale
    step = 0.3  # Scale increment

    def expand():
        nonlocal scale
        draw_heart(canvas, scale)
        scale += step
        if scale <= max_scale:
            canvas.after(30, expand)  # Repeat every 30 ms

    expand()

# Create the main tkinter window
root = tk.Tk()
root.title("Try Again, Human")

# Create a canvas widget
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack(fill="both", expand=True)

# Start the animation
animate_heart(canvas)

# # Run the tkinter main loop
# root.mainloop()