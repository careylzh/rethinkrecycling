import tkinter as tk
import math


class ExpandingHeartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expanding Heart Animation")

        # Create a canvas widget
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Animation parameters
        self.scale = 1
        self.max_scale = 15
        self.step = 0.3

        # Start the animation
        self.animate_heart()

    def draw_heart(self, scale, color="green"):
        # Draw a heart on the canvas with the given scale.
        self.canvas.delete("heart")  # Clear the previous heart
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_x = width // 2
        center_y = height // 2

        points = []
        for t in range(0, 360, 1):
            t_rad = math.radians(t)
            x = 16 * math.sin(t_rad) ** 3
            y = (
                13 * math.cos(t_rad)
                - 5 * math.cos(2 * t_rad)
                - 2 * math.cos(3 * t_rad)
                - math.cos(4 * t_rad)
            )
            points.append((center_x + x * scale, center_y - y * scale))

        for i in range(len(points) - 1):
            self.canvas.create_line(
                points[i], points[i + 1], fill=color, tags="heart", width=2
            )

        # Add the "Thank you" text below the heart
        self.draw_text(center_x, center_y + scale * 18, "Thank you for recycling, you have won my heart")

    def draw_text(self, x, y, text, color="green", font=("Arial", 15)):
        # Draw text on the canvas.
        self.canvas.delete("text")  # Clear previous text
        self.canvas.create_text(
            x, y, text=text, fill=color, font=font, tags="text"
        )

    def animate_heart(self):
        # Animate the expanding heart. 
        def expand():
            self.draw_heart(self.scale)
            self.scale += self.step
            if self.scale <= self.max_scale:
                self.canvas.after(30, expand)  # Repeat every 30 ms

        expand()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpandingHeartApp(root)
    root.mainloop()
