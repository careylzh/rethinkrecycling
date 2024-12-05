#default python modules
import RPi.GPIO as GPIO
from time import sleep
import random 
import tkinter as tk

#internal software modules 
from lose_animation import LoseAnimation
from rewards import *
from sample_codes.animations_integration_test.animation_classes_test import *
from phone_number_screen import PhoneNumberScreen

total_prize_pool = 5.00
switch_in = 12 # to update
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_in, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def calculate_reward():
     probability_list = [0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.15]
     sleep(1)
     chosen_prize = random.choice(probability_list)
     print("chosen_prize: ", chosen_prize)
     calculate_reward_amount = round(chosen_prize*total_prize_pool,2)
     return calculate_reward_amount

def run_animations(x):
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
          current_animation.start(run_animations(x))  # Start current animation

def run_animations_phone_number_screen(x):
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

# def gamble_start_test(x):
#     print("gambling app has started")
#     return



while True:

     # Initialize animations
     root = tk.Tk()
     root.wm_attributes('-fullscreen', 'True')
     canvas = tk.Canvas(root, width=1280, height=800, bg="white")
     canvas.pack()

     #TODO: refactor this section when GPIO wiring code is complete.

     
     animations = [SplashScreen(canvas)]
     run_animations(1)
     calculate_reward_amount=calculate_reward()
     animations = [PhoneNumberScreen(canvas, calculate_reward_amount)]
     GPIO.add_event_detect(switch_in, GPIO.BOTH, callback=run_animations_phone_number_screen, bouncetime=500)
     # USER_PULLS_SLOT_MACHINE_HANDLE = GPIO.event_detected(switch_in)

     # USER_PULLS_SLOT_MACHINE_HANDLE = True

     # if(USER_PULLS_SLOT_MACHINE_HANDLE == True):
     canvas.delete("all")
     # run_animations()
     # USER_PULLS_SLOT_MACHINE_HANDLE = False
          
     root.mainloop()
     # print("code pauses at animation loop")
     # root.destroy()


'''
TODO:
- destroy animation on the canvas after phone number submission, play splash screen
'''