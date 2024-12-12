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
# def initiate_crushing(x):
#     global root
#     global canvas
#     global bg_label
#     print("user pushed lever. initiate_crushing called...\n")
#     bg_label.destroy()
#     current_background_image = ImageTk.PhotoImage(file=background_images[1])
#     bg_label = tk.Label(root, image=current_background_image)
#     bg_label.place(relwidth=1, relheight=1)
#     canvas.pack()

#     #  global total_prize_pool
#     #  total_prize_pool += 0.10
#     #  total_prize_pool = round(total_prize_pool,2)
#     #  print("total prize pool", total_prize_pool)
#     #  # update_text()
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

def initiate_push():
    global i
    # global root
    # global canvas
    # global bg_label
    print("user pushed lever. initiate_crushing called...\n")
    # bg_label.destroy()
    # OLD
    # bg_label.destroy()
    # current_background_image = ImageTk.PhotoImage(file=background_images[1])
    # bg_label = tk.Label(root, image=current_background_image, tags="bg_label")
    # bg_label.place(relwidth=1, relheight=1)
    # bg_label.pack()

    for i in range(0,3):
        # i+=1
        print("tracking i in push: ", i)
        new_image = Image.open(background_images[i])
        new_tk_image = ImageTk.PhotoImage(new_image)
        bg_label.configure(image=new_tk_image)
        bg_label.image = new_tk_image  # Update reference to avoid garbage collection
        sleep(0.5)
    # if(i==2):
    #     i=0
    return

US_sensor_trig = 22
US_sensor_ech = 11
push_screen_on = 0
lever_active = 0

def run_us_sensor():
     GPIO.setup(US_sensor_trig, GPIO.OUT)
     GPIO.setup(US_sensor_ech, GPIO.IN)
     global push_screen_on
     global lever_active
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

        if (distance < 18 and push_screen_on == 0 and lever_active == 0) :
            sleep(1)
            initiate_push()
            push_screen_on = 1
            lever_active = 1 

        elif (distance > 18 and push_screen_on == 1):
            new_image = Image.open(background_images[0]) #show default bg screen
            new_tk_image = ImageTk.PhotoImage(new_image)
            bg_label.configure(image=new_tk_image)
            bg_label.image = new_tk_image  # Update reference to avoid garbage collection
            push_screen_on = 0
            lever_active = 0
            
        sleep(1)

def initiate_pull(x):
    global i
    print("user pulled lever. initiate_gameplay called...\n")     
    
    # global total_prize_pool
    # new_image = Image.open(background_images[9])
    # new_tk_image = ImageTk.PhotoImage(new_image)
    # bg_label.configure(image=new_tk_image)
    # bg_label.image = new_tk_image

    for i in range(3,10):
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
        new_image = Image.open(background_images[10]) #show "thank you for recycling" screen
        new_tk_image = ImageTk.PhotoImage(new_image)
        bg_label.configure(image=new_tk_image)
        bg_label.image = new_tk_image  # Update reference to avoid garbage collection
    else:
        new_image = Image.open(background_images[15]) #show "Big Win!" screen
        new_tk_image = ImageTk.PhotoImage(new_image)
        bg_label.configure(image=new_tk_image)
        bg_label.image = new_tk_image  # Update reference to avoid garbage collection
    # global i
    # i=9
    sleep(2)
    new_image = Image.open(background_images[0]) #show default bg screen
    new_tk_image = ImageTk.PhotoImage(new_image)
    bg_label.configure(image=new_tk_image)
    bg_label.image = new_tk_image  # Update reference to avoid garbage collection
    
    #for us sensor
    global lever_active
    lever_active = 0
    global push_screen_on
    push_screen_on = 0
    return

    # sleep(2)
    # new_image = Image.open("2-background-no-prize.png").resize((1280, 800))
    # new_tk_image = ImageTk.PhotoImage(new_image)
    # bg_label.configure(image=new_tk_image)
    # bg_label.image = new_tk_image

#DEFINE states = 1,2,3,4,5 
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

# global total_prize_pool
# total_prize_pool = 5.00
# global root
# global canvas
root = tk.Tk()
root.wm_attributes('-fullscreen', 'True')
# canvas = tk.Canvas(root, width=1280, height=800, bg="black")
# canvas.pack()

# background_images = ["1-background.png","2-background.png","4-background.png","5-background-no-prize.png", "5-background-win.png"]
# background_images = [
#     f"test{i}.png" for i in range(1, 24)
# ]
# background_images = [
#     "Artboard 1 copy.png","Artboard1.png"
# ]
background_images = [
    f"{i}.png" for i in range(1, 24)
]
print(background_images)

GPIO.add_event_detect(switch_in, GPIO.RISING, callback=initiate_pull, bouncetime=500) 
#GPIO.add_event_detect(switch_in_crushing, GPIO.RISING, callback=initiate_push, bouncetime=500) --> replaced by us sensor 

current_background_image = ImageTk.PhotoImage(file=background_images[0])
# global bg_label 
bg_label = tk.Label(root, image=current_background_image)
bg_label.pack()
# bg_label.place(relwidth=1, relheight=1)
# bg_label.pack()


    #  global total_prize_pool
    #  total_prize_pool += 0.10
    #  total_prize_pool = round(total_prize_pool,2)
    #  print("total prize pool", total_prize_pool)
    #  # update_text()

# def initiate_gameplay(x):
#     print("user pulled lever. initiate_gameplay called...\n")
#     global total_prize_pool

#async interruptions which trigger screen animations by changing SCREEN_STATE - placing a bottle (ultrasonic) and    


#insert bottle, sleep(2)

#CODE SNIPPET for each screen
# current_background_image = ImageTk.PhotoImage(file=background_images[1])
# bg_label = tk.Label(root, image=current_background_image)
# bg_label.place(relwidth=1, relheight=1)
# bg_label.destroy()
# sleep(2)

#no-prize
# current_background_image = ImageTk.PhotoImage(file=background_images[2])
# bg_label = tk.Label(root, image=current_background_image)
# bg_label.place(relwidth=1, relheight=1)
# bg_label.pack()
# bg_label.destroy()
# sleep(2)

### Us sensor initialisation
sensor_thread = threading.Thread(target=run_us_sensor)
sensor_thread.start()

root.mainloop()
    #win
    # current_background_image = ImageTk.PhotoImage(file=background_images[3])
    # bg_label = tk.Label(root, image=current_background_image)
    # bg_label.place(relwidth=1, relheight=1)
    # bg_label.destroy()


   #in each of the screens below, add and delete the following images

##uncomment if you need to revise the PROGRAM FLOW
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

    


