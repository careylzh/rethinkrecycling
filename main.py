#default python modules
#import RPi.GPIO as RPI
from time import sleep
import random 
import tkinter as tk
from PIL import Image, ImageTk


import RPi.GPIO as GPIO
switch_in = 12 # to update
switch_in_crushing = 16
red_led_pin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_in, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_in_crushing, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(switch_in_for_redlight, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.output(red_led_pin, 0)

#for ultrasonic sensor
US_sensor_trig = 22
US_sensor_ech = 32
from gpiozero import DistanceSensor

global sensor 
sensor = DistanceSensor(trigger=US_sensor_trig, echo=US_sensor_ech)

def run_us_sensor():
     global sensor
     while True:
          # Wait 2 seconds
          sleep(2)
          
          # Get the distance in metres
          distance = sensor.distance

          # But we want it in centimetres
          distance = sensor.distance * 100

          # We would get a large decimal number so we will round it to 2 places
          distance = round(sensor.distance, 2)

          # Print the information to the screen
          print("Distance: {} cm".format(sensor.distance))

#internal software modules 
from rewards import *
from animation_classes_library import *
from phone_number_screen import PhoneNumberScreen

total_prize_pool = 5.00
bottle_count = 0

def calculate_reward():
     global total_prize_pool
     probability_list = [0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.15]
     sleep(1)
     chosen_prize = random.choice(probability_list)
     print("chosen_prize: ", chosen_prize)
     calculate_reward_amount = round(chosen_prize*total_prize_pool,2)
     total_prize_pool -= calculate_reward_amount
     total_prize_pool = round(total_prize_pool,2)
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

def initiate_crushing(x):
     print("initiate_crushing called...\n")
     global total_prize_pool
     total_prize_pool += 0.10
     total_prize_pool = round(total_prize_pool,2)
     print("total prize pool", total_prize_pool)
     # update_text()
     after_submit_update_text()
     GPIO.output(red_led_pin, 1)

def initiate_gameplay(x):
     print("initiate_gameplay called...\n")
     global total_prize_pool
     global bottle_count
     if bottle_count != 0:
          canvas.delete("after_submit_screen_butt")
          canvas.delete("splash_screen_prize_pool_text")
          calculate_reward_amount=calculate_reward()
          animations = [
                    # SplashScreen(canvas),
                    LoadingScreen(canvas, calculate_reward_amount),
                    PhoneNumberScreen(canvas, calculate_reward_amount, total_prize_pool, root),

          ]
          run_animations(animations)
          bottle_count = 0

# def update_text():
#     entry = tk.Entry(root)
#     new_text = entry.get()  # Get the text from the entry widget
#     canvas.itemconfig(splash_screen_prize_pool_text, text=f'Insert 1 Bottle to Begin! \n Prize Pool: {total_prize_pool}')  # Update the text

def after_submit_update_text():
     global bottle_count
     global after_submit_screen_butt
     global splash_screen_prize_pool_text
     if bottle_count == 0:
          canvas.delete("after_submit_screen_butt")
          canvas.delete("splash_screen_prize_pool_text")
          after_submit_screen_butt = canvas.create_text(
               400, 100,  # Coordinates: x=400, y=100
               text=f'Insert 1 Bottle to Begin! \n Prize Pool: {total_prize_pool}',  # The text to display
               font=("Arcade", 20),  # Font and size
               fill="green",
                 tags="after_submit_screen_butt"  # Text color
               )
          bottle_count += 1
     else:
          canvas.delete("after_submit_screen_butt")
          canvas.delete("splash_screen_prize_pool_text")
          after_submit_screen_butt = canvas.create_text(
               400, 100,  # Coordinates: x=400, y=100
               text=f'Insert 1 Bottle to Begin! \n Prize Pool: {total_prize_pool}',  # The text to display
               font=("Arcade", 20),  # Font and size
               fill="green",
                 tags="after_submit_screen_butt"  # Text color
               )
          # canvas.itemconfig(after_submit_screen_butt, text=f'Insert 1 Bottle to Begin! \n Prize Pool: {total_prize_pool}')  # Update the text
          bottle_count += 1

def red_light_off(x):
     GPIO.output(red_led_pin, 0)

while True:

     # Initialize animations
     global root
     root = tk.Tk()
     root.wm_attributes('-fullscreen', 'True')
     global canvas
     canvas = tk.Canvas(root, width=1280, height=800, bg="white")
     
     image_path = "background.png"
     bg_image = Image.open(image_path)
     bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  # Use the new Resampling constant
     bg_image_tk = ImageTk.PhotoImage(bg_image)

     # Add the image to the canvas
     canvas.create_image(0, 0, anchor=tk.NW, image=bg_image_tk)
     global splash_screen_prize_pool_text
     splash_screen_prize_pool_text = canvas.create_text(
          400, 100,  # Coordinates: x=400, y=100
          text=f'Insert 1 Bottle to Begin! \n Prize Pool: {total_prize_pool}',  # The text to display
          font=("Arcade", 20),  # Font and size
          fill="white",  # Text color
          tags="splash_screen_prize_pool_text"
          )    
     canvas.pack()
     run_us_sensor()

     USER_PULLS_SLOT_MACHINE_HANDLE = True
     # animations = [SplashScreen(canvas)]
     GPIO.add_event_detect(switch_in, GPIO.RISING, callback=initiate_gameplay, bouncetime=500)
     GPIO.add_event_detect(switch_in_crushing, GPIO.RISING, callback=initiate_crushing, bouncetime=500)
     #GPIO.add_event_detect(switch_in_for_redlight, GPIO.FALLING, callback=red_light_off, bouncetime=500)

     root.mainloop()
     print("code passes mainloop()")
     root.destroy()