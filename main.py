import time
import webbrowser

print(f"K-pop Idol Dating Game\n")
print(f"Developed by Kimono きもの\n")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print(f"Welcome to your new adventure! The elder gods have sent you to a very important quest.\n"
      f"You will date a k-pop idol (he / she is waiting for you), but the grizzly bear is out there to kill your dreams!\n"
      f"Your mission is to avoid the grizzly bear so you can go on a date with your husband / wife)")

name = input("What is your name?\n")
print(f"Hi {name}! Good to have you on board!\n")
time.sleep(2)
print(f"All of a sudden you woke up in this weird forest."
      f" You just heard a strange sound from your right ear.\n")

decision_left_or_right = input("Which path will you take to get out of here? Left or right\n")

if decision_left_or_right.lower() == "left":
      print(f"Phew! You got out of there\n")
      time.sleep(2)
      print(f"What's that roar?!")
      time.sleep(2)
      print(f"I guess there's nothing I have to worry about. I have to go to my date. I still look like a mess T_T")
      print(f"Alright, now what shall I do? If I'm going to swim my clothes are going to be messed up for the date.")

      swim_or_wait = input(f"Swim or wait?\n")

      if swim_or_wait.lower() == "swim":
            print(f"You made it! Good job! But your clothes are soaking wet now.")

      elif swim_or_wait.lower() == "wait":
            print(f"The heck is that?!")
            time.sleep(2)
            print(f"Aaaahhhhh!!!")
            print(f"Game over!")
            print("Run this file again if you want to play this game again!")

      else:
            print(f"The Elder Gods have sent you to hell.")
            print(f"Game over!")
            print("Run this file again if you want to play this game again!")

      print(f"You finally made out of this weird forest. Now you are in some futuristic city.")
      time.sleep(3)
      print(f"Wait I'm in Seoul??? I can't believe it!")
      time.sleep(2)
      print(f"Your inner Koreaboo is growing exponentially.")
      time.sleep(2)
      print(f"You have arrived at SM Entertainment to pick up your date.\n"
            f"There are 3 doors in front of you.")

      final_decision = input("Which door will you open? Pick red, blue or yellow\n")

      if final_decision.lower() == "red":
            print(f"What the heck?! A panda bear?")
            time.sleep(2)
            print(f"Aaaahhhhh!!!")
            time.sleep(2)
            print(f"Game over!")
            print("Run this file again if you want to play this game again!")

      elif final_decision.lower() == "blue":
            print(f"So we finally meet hooman!")
            time.sleep(2)
            print(f"Since when do Grizzly Bears know how to talk?")
            time.sleep(2)
            print(f"Aaaahhhhh!!!")
            time.sleep(2)
            print(f"Game over!")
            print("Run this file again if you want to play this game again!")

      elif final_decision.lower() == "yellow":
            print(f"You made it to your date with Irene")
            time.sleep(2)
            print(f"You are eating with Irene now and she wants to be your girlfriend")
            time.sleep(3)
            print(f"Irene liked her first date with you {name}. She wants to date again!")
            print("You have completed the game!")
            time.sleep(4.5)
            webbrowser.open_new('https://www.youtube.com/watch?v=Iuh6nUFM-cs')
            print(f"Developed by Kimono きもの")

      else:
            print(f"The Elder Gods have sent you to hell.")
            print(f"Game over!")
            print("Run this file again if you want to play this game again!")

elif decision_left_or_right.lower() == "right":
      print(f"Crap!!! It's a Grizzly Bear!!")
      time.sleep(2)
      print(f"Aaaahhhhh!!!")
      print(f"Game over. {name} won't go on a date with a k-pop idol. Better luck next time ;)")
      print("Run this file again if you want to play this game again!")

else:
      print(f"The Elder Gods have sent you to hell.")
      print(f"Game over!")
      print("Run this file again if you want to play this game again!")
