#import libs
from time import sleep
import random 
import tkinter as tk
from PIL import Image, ImageTk

#internal software modules 
from rewards import *
# from animation_classes_library import *
from phone_number_screen import PhoneNumberScreen
import threading

i=0
total_prize_pool = 5.00

def calculate_reward():
     global total_prize_pool
     probability_list = [0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.15]
    #  sleep(1)
     chosen_prize = random.choice(probability_list)
     print("chosen_prize: ", chosen_prize)
     calculate_reward_amount = round(chosen_prize*total_prize_pool,2)
     total_prize_pool -= calculate_reward_amount
     total_prize_pool = round(total_prize_pool,2)
     return calculate_reward_amount

def initiate_push_instructions():
    global i
    print("Bottle detected. waiting for user to push lever...\n")

    for i in range(0,3):
        print("tracking i in push: ", i)
        new_image = Image.open(background_images[i])
        new_tk_image = ImageTk.PhotoImage(new_image)
        bg_label.configure(image=new_tk_image)
        bg_label.image = new_tk_image  # Update reference to avoid garbage collection
        sleep(0.5)

    return

def initiate_push(x):
    global i
    global pacman_active
    global pull_instruction_on
    if(push_instruction_on == 1):
        print("user pushed lever. initiate_crushing called...\n")

        pacman_active = 1
        for i in range(4,12):
            # i+=1
            print("tracking i in push: ", i)
            new_image = Image.open(background_images[i])
            new_tk_image = ImageTk.PhotoImage(new_image)
            bg_label.configure(image=new_tk_image)
            bg_label.image = new_tk_image  # Update reference to avoid garbage collection
            sleep(0.5)

        pull_instruction_on = 1
    pacman_active = 0
    return

US_sensor_trig = 22
US_sensor_ech = 11
push_instruction_on = 0
lever_active = 0
pacman_active = 0
pull_instruction_on = 0
def run_us_sensor():
     GPIO.setup(US_sensor_trig, GPIO.OUT)
     GPIO.setup(US_sensor_ech, GPIO.IN)
     global push_instruction_on
     global lever_active
     global pull_instruction_on
     global pacman_active
     while True:
        GPIO.output(US_sensor_trig, GPIO.LOW)
        print ("Waiting for sensor to settle")
        print ("Calculating distance")

        GPIO.output(US_sensor_trig, GPIO.HIGH)
        sleep(0.00001)
        GPIO.output(US_sensor_trig, GPIO.LOW)

        while GPIO.input(US_sensor_ech)==0:
            #print("echo 0")
            pulse_start_time = time.time()
        while GPIO.input(US_sensor_ech)==1:
            #print("echo 1")
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print ("Distance:",distance,"cm")

        if (pull_instruction_on == 0 and pacman_active == 0):

            if (distance < 11 and push_instruction_on == 0) :
                sleep(1)
                initiate_push_instructions()
                push_instruction_on = 1

            elif (distance > 11 and push_instruction_on == 1):
                new_image = Image.open(background_images[0]) #show default bg screen
                new_tk_image = ImageTk.PhotoImage(new_image)
                bg_label.configure(image=new_tk_image)
                bg_label.image = new_tk_image  # Update reference to avoid garbage collection
                push_instruction_on = 0

        sleep(1)

def initiate_pull(x):
    global i
    global pacman_active
    global pull_instruction_on
    global lever_active

    if (pull_instruction_on == 1):
        
        print("user pulled lever. initiate_gameplay called...\n")     

        for i in range(13,15):
            # i+=1
            print("tracking i in pull: ", i)
            new_image = Image.open(background_images[i])
            new_tk_image = ImageTk.PhotoImage(new_image)
            bg_label.configure(image=new_tk_image)
            bg_label.image = new_tk_image  # Update reference to avoid garbage collection
            sleep(0.5)

        #generate random reward amount
        calculate_reward_amount = calculate_reward()
        if calculate_reward_amount <= 0:
            new_image = Image.open(background_images[21]) #show "Oops! Good luck next time." screen
            new_tk_image = ImageTk.PhotoImage(new_image)
            bg_label.configure(image=new_tk_image)
            bg_label.image = new_tk_image  # Update reference to avoid garbage collection
        else:
            new_image = Image.open(background_images[15]) #show "Big Win!" screen
            new_tk_image = ImageTk.PhotoImage(new_image)
            bg_label.configure(image=new_tk_image)
            bg_label.image = new_tk_image  # Update reference to avoid garbage collection

        sleep(2)
        new_image = Image.open(background_images[0]) #show default bg screen
        new_tk_image = ImageTk.PhotoImage(new_image)
        bg_label.configure(image=new_tk_image)
        bg_label.image = new_tk_image  # Update reference to avoid garbage collection
        
        #for us sensor
        lever_active = 0
        pull_instruction_on = 0
        
    return
'''
screens: 
1 - 
2 
3
4
5

'''
# SCREEN_STATE = 1
import time
import RPi.GPIO as GPIO
switch_in = 12 # to update
switch_in_crushing = 16
switch_in_for_redlight = 16
red_led_pin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_in, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_in_crushing, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(switch_in_for_redlight, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.output(red_led_pin, 0)

root = tk.Tk()
root.wm_attributes('-fullscreen', 'True')

background_images = [
    f"{i}.png" for i in range(1, 24)
]
print(background_images)

GPIO.add_event_detect(switch_in, GPIO.RISING, callback=initiate_push, bouncetime=500) 
GPIO.add_event_detect(switch_in_crushing, GPIO.RISING, callback=initiate_pull, bouncetime=500)

current_background_image = ImageTk.PhotoImage(file=background_images[0])
bg_label = tk.Label(root, image=current_background_image)
bg_label.pack()

sensor_thread = threading.Thread(target=run_us_sensor)
sensor_thread.start()

root.mainloop()


##READ the code below if you need to revise the PROGRAM FLOW
    # if SCREEN_STATE == 1: 
    #     pass  
    #     #always create elements with a tag
    #     #destroy respective elements by referencing tag
    # elif SCREEN_STATE == 2:
    #     sleep(2)
    #     pass
    #     #always create elements with a tag
    #     #destroy respective elements by referencing tag
    # elif SCREEN_STATE == 3:
    #     pass
    #     #always create elements with a tag
    #     #destroy respective elements by referencing tag
    # elif SCREEN_STATE == 4:
    #     pass 
    #     #always create elements with a tag
    #     #destroy respective elements by referencing tag
    # elif SCREEN_STATE == 5:
    #     #calculate reward
    #     #call phone_number_screen_refactor, pass reward into screen

    #     if calculate_reward == 0:
    #         #display "losing" screen
    #         #destroy screen after 2 seconds
    #         sleep(2)
    #         SCREEN_STATE = 5
    #         pass
    #     else:
    #         #display "winning screen" with phone number
    #         pass

    


