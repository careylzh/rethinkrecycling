#import libs
from time import sleep
import random 
import tkinter as tk
from PIL import Image, ImageTk

#internal software modules 
from rewards import *
# from animation_classes_library import *
from phone_number_screen import PhoneNumberScreen

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

def initiate_crushing(x):
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

    new_image = Image.open("Win Bin UIUX screens-01.png").resize((1280, 800))
    new_tk_image = ImageTk.PhotoImage(new_image)
    bg_label.configure(image=new_tk_image)
    bg_label.image = new_tk_image  # Update reference to avoid garbage collection


def initiate_gameplay(x):
    print("user pulled lever. initiate_gameplay called...\n")
    # global total_prize_pool
    new_image = Image.open("Win Bin UIUX screens-02.png").resize((1280, 800))
    new_tk_image = ImageTk.PhotoImage(new_image)
    bg_label.configure(image=new_tk_image)
    bg_label.image = new_tk_image

    # sleep(2)
    # new_image = Image.open("2-background-no-prize.png").resize((1280, 800))
    # new_tk_image = ImageTk.PhotoImage(new_image)
    # bg_label.configure(image=new_tk_image)
    # bg_label.image = new_tk_image

#DEFINE states = 1,2,3,4,5 
'''
screens: 
1 - 
2 
3
4
5

'''
# SCREEN_STATE = 1

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
# root.wm_attributes('-fullscreen', 'True')
# canvas = tk.Canvas(root, width=1280, height=800, bg="white")
# canvas.pack()

# background_images = ["1-background.png","2-background.png","4-background.png","5-background-no-prize.png", "5-background-win.png"]
background_images = [
    f"Win Bin UIUX screens-{str(i).zfill(2)}.png" for i in range(1, 26)
]

GPIO.add_event_detect(switch_in, GPIO.RISING, callback=initiate_gameplay, bouncetime=500)
GPIO.add_event_detect(switch_in_crushing, GPIO.RISING, callback=initiate_crushing, bouncetime=500)

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

    


