import tkinter as tk
from PIL import Image, ImageTk  # Import from Pillow

# Create the main window
root = tk.Tk()
# Load the image
tk_image = ImageTk.PhotoImage(file="1-background.png")  # Replace with your image file

# Create a Label to display the image
label1 = tk.Label(root, image=tk_image)
label1.pack()
def change_image():
    new_image = Image.open("5-background-win.png").resize((1280, 800))
    new_tk_image = ImageTk.PhotoImage(new_image)
    label1.configure(image=new_tk_image)
    label1.image = new_tk_image  # Update reference to avoid garbage collection

button = tk.Button(root, text="Change Image", command=change_image)
button.pack()

root.mainloop()

