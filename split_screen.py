import tkinter as tk

class MyApp:
    def __init__(self, root):
        # Configure grid to split the screen into two halves
        root.columnconfigure(0, weight=1)  # Left column
        root.columnconfigure(1, weight=1)  # Right column
        
        root.rowconfigure(0, weight=1)  # Single row fills the window

        # Create the label for the left side
        left_label = tk.Label(
            root, 
            text="This is the left half", 
            fg="white",  # Text color
            bg="blue",   # Background color
            anchor="center"
        )
        left_label.grid(row=0, column=0, sticky="nsew")  # Fill the left half

        # Right side remains empty
        # No widgets in column 1

root = tk.Tk()

# Set the window to fill the screen size
root.geometry("800x400")  # Example size; adjust for your screen

app = MyApp(root)
root.mainloop()
