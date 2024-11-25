#default python modules
#import RPi.GPIO as 
from time import sleep
import random 

#internal software modules 
from loading_screen import LoadingScreen
from win_animation_circle_with_text import WinAnimation

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
          calculate_reward_amount = int(chosen_prize*total_prize_pool)
          return calculate_reward_amount

     #displays win animations
     calculate_reward_amount=calculate_reward()
     if(calculate_reward_amount == 0):          
          app = WinAnimation(calculate_reward_amount)
          app.mainloop()