import tkinter as tk
from rewards import *
class PhoneNumberScreen:
    def __init__(self, canvas, calculated_reward_amount, total_prize_pool):
        self.canvas = canvas
        self.display = None
        self.running = False
        self.instruction_label = None
        self.calculated_reward_amount = calculated_reward_amount
        self.calculated_reward_string = None
        self.total_prize_pool = total_prize_pool

    def start(self):
        # print("callback in phone number screen: ", callback)
        self.canvas.delete("all")  # Deletes all objects on the canvas
        print("start in PhoneNumberScreen called")

        # Create a display to show the numbers being pressed
        if(self.calculated_reward_amount == 0):
            self.instruction_label = tk.Label(
                self.canvas, text=f"Bottle processed! You have won another chance to recycle. Key in your phone number and receive rewards at the end of today. Happy recycling!",
                font=("Helvetica", 16), wraplength=300, justify="center"
            )
        else:
            self.instruction_label = tk.Label(
                self.canvas, text=f"Bottle processed! You have won ${self.calculated_reward_amount}. Key in your phone number and receive rewards at the end of today. Happy recycling!",
                font=("Helvetica", 16), wraplength=300, justify="center"
            )
       
        self.instruction_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))
    
        self.running = True
        self.display = tk.Entry(self.canvas, font=("Helvetica", 24), justify="right")
        self.display.grid(row=1, column=0, columnspan=3, ipadx=10, ipady=10, padx=5, pady=5)

        # Keypad buttons
        self.create_keypad()
        # self.callback = callback
        
    def create_keypad(self):
        # Layout for keypad
        buttons = [
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
            ('0', 5, 1)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(
                self.canvas, text=text, font=("Helvetica", 10),
                command=lambda t=text: self.button_pressed(t), width=4, height=2
            )
            button.grid(row=row, column=col, padx=5, pady=5)
            
        # Clear button
        clear_button = tk.Button(
            self.canvas, text="C", font=("Helvetica", 10),
            command=self.clear_display, width=4, height=2
        )
        clear_button.grid(row=5, column=0, padx=5, pady=5)

        # Submit button
        submit_button = tk.Button(
            self.canvas, text="Submit", font=("Helvetica", 10),
            command=self.submit_display, width=8, height=2
        )
        submit_button.grid(row=5, column=2, padx=5, pady=5)
        
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
        #Ask for user input and write phone number and reward to CSV
        write_to_csv(self.calculated_reward_amount, current_text)
        self.clear_display()
        self.canvas.delete("all", tk.END)
        for widget in self.canvas.winfo_children():
            widget.destroy()

        self.canvas.create_text(
          200, 100,  # Coordinates: x=200, y=100
          text=f"Insert 1 Bottle to Begin! \n Prize Pool: {total_prize_pool}",  # The text to display
          font=("Arcade", 20),  # Font and size
          fill="green"  # Text color
          )
        self.canvas.pack()
        # self.callback()

# if __name__ == "__main__":
#     canvas = tk.Tk()
#     app = PhoneNumberScreen(canvas)
#     canvas.mainloop()
