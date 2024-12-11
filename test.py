from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

# Create the main window
root = Tk()

# Initial image
initial_image = Image.open("1-background.png").resize((1280, 800))
initial_tk_image = ImageTk.PhotoImage(initial_image)

# Label to display the image
label1 = Label(root, image=initial_tk_image)
label1.image = initial_tk_image  # Keep a reference to the image
label1.pack()

# Function to change the image
def change_image():
    new_image = Image.open("5-background-win.png").resize((1280, 800))
    new_tk_image = ImageTk.PhotoImage(new_image)
    label1.configure(image=new_tk_image)
    label1.image = new_tk_image  # Update reference to avoid garbage collection

# Button to trigger the image change
button = Button(root, text="Change Image", command=change_image)
button.pack()

root.mainloop()
