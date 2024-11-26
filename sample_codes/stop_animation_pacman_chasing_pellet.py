import tkinter as tk

calculated_amount = 0

def move_pacman():
    global pacman_open
    canvas.move(pacman, 20, 0)
    pacman_coords = canvas.coords(pacman)
    pellet_coords = canvas.coords(pellet)

    # Check collision with the pellet
    if pacman_coords[2] >= pellet_coords[0]:
        canvas.delete(pellet)
        canvas.create_text(250, 150, text='Congratulations Human, you have won {calculated_amount}', font=("Arial", 10), fill="white")

    # Toggle Pacman mouth
    if pacman_open:
        canvas.itemconfig(pacman, start=45, extent=270)
    else:
        canvas.itemconfig(pacman, start=0, extent=360)
    pacman_open = not pacman_open

    # Loop animation
    if pacman_coords[2] < 500:
        root.after(100, move_pacman)

# Create the main window
root = tk.Tk()
root.title("Pacman Chasing Pellet")
canvas = tk.Canvas(root, width=500, height=200, bg="black")
canvas.pack()

# Create Pacman
pacman = canvas.create_arc(50, 50, 100, 100, start=45, extent=270, fill="yellow", outline="yellow")
pacman_open = True

# Create Pellet
pellet = canvas.create_oval(400, 75, 420, 95, fill="white", outline="white")

# Start the animation
move_pacman()

root.after(3, stop_animation)

# Run the Tkinter event loop
root.mainloop()
