#default python modules
#import RPi.GPIO as RPI
from time import sleep
import random 
import tkinter as tk

#internal software modules 
from loading_screen import LoadingScreen
from lose_animation import LoseAnimation
from rewards import *
from sample_codes.animations_integration_test.animation_classes_test import *

total_prize_pool = 5.00

def calculate_reward():
     probability_list = [0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.15]
     sleep(1)
     chosen_prize = random.choice(probability_list)
     print("chosen_prize: ", chosen_prize)
     calculate_reward_amount = round(chosen_prize*total_prize_pool,2)
     return calculate_reward_amount

def run_animations(animations, calculate_reward_amount):
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
          current_animation.start(run_animations)  # Start current animation

while True:

     # Initialize animations
     root = tk.Tk()
     canvas = tk.Canvas(root, width=1280, height=800, bg="white")
     canvas.pack()

     #TODO: refactor this section when GPIO wiring code is complete.
     USER_PULLS_SLOT_MACHINE_HANDLE = True 
     if(USER_PULLS_SLOT_MACHINE_HANDLE == True):
          calculate_reward_amount=calculate_reward()
          animations = [
               AnimationB(canvas),
               LoadingScreen(canvas, calculate_reward_amount)
          ]
          run_animations(animations, calculate_reward_amount)
          USER_PULLS_SLOT_MACHINE_HANDLE = False

          #Ask for user input and write phone number and reward to CSV
          # phone_number = input("Kindly key in your phone number to redeem the prize")
          # write_to_csv(calculate_reward_amount, phone_number)
          
     root.mainloop()
     root.destroy()