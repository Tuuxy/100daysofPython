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
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************

'''
)

print("Welcome to Treasure Island. Your mission is to find the treasure!")
direction = input("You're at a crossroad, where do you want to go? Left or Right?\n")
if direction.lower() != "left":
    print("You fall into a hole. Game Over!")
else:
    action = input("You've come to a lake.\nThere is an island in the middle of the lake.\nType \"Wait\" to wait for a boat, or type \"Swim\" to swim across.\n")
    if action.lower() != "wait":
        print("You got attacked by an angry trout. Game Over!")
    else:
        door = input("You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one blue and a yellow one.\nWhich one do you choose? \"Red\", \"Blue\" or \"Yellow\"?\n")
        if door.lower() == "red":
            print("It's a room full of fire. Game over!")

        elif door.lower() == "blue":
            print("You enter the room and you are eaten by beasts. Game Over!")

        elif door.lower() == "yellow":
            print("You found the treasure. You Win!")
            
        else :
            print("You Lose!")
            