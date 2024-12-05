import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Canvas Background Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Load an image using PIL (for formats like JPEG/PNG)
# Replace 'background.jpg' with the path to your image
image_path = "background.jpg"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)  # Use the new Resampling constant
bg_image_tk = ImageTk.PhotoImage(bg_image)

# Add the image to the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image_tk)

# Add some widgets or drawings to the canvas
canvas.create_text(300, 50, text="Hello, Canvas!", font=("Arial", 24), fill="white")

# Run the application
root.mainloop()
