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
while True:
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    option1=input("left or right ? ").lower()
    if option1=="right" : 
        print("Fall into a hole.Game Over.")
    elif option1=="left":
        option2=input("swim or wait:").lower() 
        if option2=="swim": 
         print("Attacked by trout. Game Over.")
        elif option2=="wait" : 
         print("which floor ? ")
         op3=input("red or blue or yellow or anything else").lower()
         if op3=="red":
            print("Burned by fire.Game Over")
         elif op3=="blue": 
            print("Eaten by beasts.Game Over.")
         elif op3=="yellow" : 
            print("You Win!") 
         else :
            print("Game Over.")
        else:
         print("Attacked by trout. Game Over.")
    else : 
        print("Fall into a hole.Game Over.")
        









