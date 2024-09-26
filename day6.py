# Challenge is here : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    while not is_facing_north:
        turn_left()
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        
    elif wall_in_front():
        turn_left()
        
    else :
        move()