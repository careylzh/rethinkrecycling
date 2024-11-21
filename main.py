#import RPi.GPIO as RPi
from time import sleep
import random 
total_prize_pool = 5.00
while True:
     #plays animation for loading
     

     #calculates reward
     probability_list = [0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.15]
     sleep(1)
     chosen_prize = random.choice(probability_list)
     print(chosen_prize)

     #displays win animations
