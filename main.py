#default python modules
#import RPi.GPIO as 
from time import sleep
import random 

#internal software modules 
from loading_screen import LoadingScreen
from win_animation import WinAnimation

total_prize_pool = 5.00

#d

while True:
     #plays animation for loading screen
     # app = LoadingScreen()
     # print("hello")
     # app.mainloop()
     # sleep(1)

     #calculates reward
     def calculate_reward():
          probability_list = [0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.15]
          sleep(1)
          chosen_prize = random.choice(probability_list)
          print(chosen_prize)
     calculate_reward()

     #displays win animations
     app = WinAnimation(calculated_amount=10)
     