import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a label
label1 = tk.Label(root, text="Label 1")
label1.pack()

# Function to destroy label1 and add a new label
def replace_label():
    global label1  # Make sure to access the global variable
    label1.destroy()
    label1 = tk.Label(root, text="New Label")
    label1.pack()

# Button to trigger the replacement of label1
replace_button = tk.Button(root, text="Replace Label 1", command=replace_label)
replace_button.pack()

root.mainloop()
