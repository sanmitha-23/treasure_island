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
print("Welcome to Treasure Island!!!")
print("Your mission is to find the treasure.") 

direction = input("There are two ways now. Which direction would you like to take? Left or Right? \n").lower()

if direction == "left":
  choice = input("There's a mysterious sea ahead. Would you like to swim or wait for the boat? Swim or Wait? \n").lower()
  if choice == 'wait':
    print("There comes the boat. You will reach the other end very soon now. It was a wise decision though!\n")
    color = input("I see there is a house with three doors. Which color door would you like to choose? Red, Blue or Green? \n").lower()
    if color == 'red':
      print("Oops!! It's a room of fire. You die. Game Over !!\n")
    elif color == 'green':
      print("Alas!! You are into the deadliest forest of the world!! Oh no, oh no!! There's a lion coming, looks like he is hungry. You know your destiny now. Game Over!!\n")
    elif color=='blue':
      print("Woah!! I see the treasure!! Voila, you win!! The treasure is yours now!!\n")
    else:
      print("There's no door with that color. Game Over!!\n")
  else:
    print("Ahh!! You are now going to be a crocodile's meal. Game Over!!\n")   
else:
  print("Urgh!! It was a trap. You fall into the ditch. Game Over!!!")
  
