#default python modules
#import RPi.GPIO as RPI
from time import sleep
import random 
import tkinter as tk

import RPi.GPIO as GPIO
switch_in = 12 # to update
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_in, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


#internal software modules 
from lose_animation import LoseAnimation
from rewards import *
from sample_codes.animations_integration_test.animation_classes_test import *
from phone_number_screen import PhoneNumberScreen

total_prize_pool = 5.00

def calculate_reward():
     probability_list = [0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.15]
     sleep(1)
     chosen_prize = random.choice(probability_list)
     print("chosen_prize: ", chosen_prize)
     calculate_reward_amount = round(chosen_prize*total_prize_pool,2)
     return calculate_reward_amount

def run_animations(animations):
     if animations:
          # control logic to displays win/lose amount and respective animations
          # print("calculate_reward_amount: ", calculate_reward_amount)
               # if(calculate_reward_amount == 0):   
               # # app = LoseAnimation(calculate_reward_amount)
               #      pass
               # elif(calculate_reward_amount > 0 and calculate_reward_amount < total_prize_pool):
               # # app = WinAnimation(calculate_reward_amount)
               #      pass
          current_animation = animations.pop(0)
          current_animation.start()  # Start current animation
          sleep(2)
          current_animation = animations.pop(0)
          current_animation.start()

def initiate_gameplay(x):
     canvas.delete("all")
     calculate_reward_amount=calculate_reward()
     animations = [
               # SplashScreen(canvas),
               LoadingScreen(canvas, calculate_reward_amount),
               PhoneNumberScreen(canvas, calculate_reward_amount),

     ]
     run_animations(animations)

while True:

     # Initialize animations
     root = tk.Tk()
     root.wm_attributes('-fullscreen', 'True')
     canvas = tk.Canvas(root, width=1280, height=800, bg="white")
     canvas.create_text(
          200, 100,  # Coordinates: x=200, y=100
          text="Insert 1 Bottle to Begin!",  # The text to display
          font=("Arcade", 20),  # Font and size
          fill="green"  # Text color
          )     
     canvas.pack()

     #TODO: refactor this section when GPIO wiring code is complete.
     USER_PULLS_SLOT_MACHINE_HANDLE = True
     # animations = [SplashScreen(canvas)]
     # run_animations()
     # if(USER_PULLS_SLOT_MACHINE_HANDLE == False):
        
     #      USER_PULLS_SLOT_MACHINE_HANDLE = False
     GPIO.add_event_detect(switch_in, GPIO.RISING, callback=initiate_gameplay, bouncetime=500)

     root.mainloop()
     root.destroy()

'''
TODO:
- destroy animation on the canvas after phone number submission, play splash screen
'''