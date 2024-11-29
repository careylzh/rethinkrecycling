import tkinter as tk

class PhoneNumberScreen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.display = None

        # Create a display to show the numbers being pressed
        self.display = tk.Entry(self.canvas, font=("Helvetica", 24), justify="right")
        self.display.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10, padx=5, pady=5)

        # Keypad buttons
        self.create_keypad()
        
    def create_keypad(self):
        # Layout for keypad
        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 1)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(
                self.canvas, text=text, font=("Helvetica", 20),
                command=lambda t=text: self.button_pressed(t), width=4, height=2
            )
            button.grid(row=row, column=col, padx=5, pady=5)
            
        # Clear button
        clear_button = tk.Button(
            self.canvas, text="C", font=("Helvetica", 20),
            command=self.clear_display, width=4, height=2
        )
        clear_button.grid(row=4, column=0, padx=5, pady=5)

        # Submit button
        submit_button = tk.Button(
            self.canvas, text="Submit", font=("Helvetica", 20),
            command=self.submit_display, width=8, height=2
        )
        submit_button.grid(row=4, column=2, padx=5, pady=5)
        
    def button_pressed(self, value):
        current_text = self.display.get()
        new_text = current_text + value
        self.display.delete(0, tk.END)
        self.display.insert(0, new_text)
        print(value)
        
    def clear_display(self):
        self.display.delete(0, tk.END)
    
    def submit_display(self):
        current_text = self.display.get()
        print(f"Submitted: {current_text}")
        self.clear_display()

# if __name__ == "__main__":
#     canvas = tk.Tk()
#     app = PhoneNumberScreen(canvas)
#     canvas.mainloop()
