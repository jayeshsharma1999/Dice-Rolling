#Author Jayesh Sharma
import pyfiglet #pip install pyfiglet
ascii_banner = pyfiglet.figlet_format("Dice Rolling Simulator BY Jayesh Sharma")
print(ascii_banner)
import random
def dice_simulate():
    number = random.randint(1,6)
    print(number)
    while(1):
       flag = str(input("Do you want to dice it up again  Enter 1 and if not enter 0 :-  "))
       if flag == '1':
         number = random.randint(1,6)
         print(number)
       else:
         print("Ending the game")
         return

dice_simulate()
