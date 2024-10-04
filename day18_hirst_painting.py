import random
from turtle import *


COLORS = [
    (1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72),
    (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170),
    (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91),
    (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218)
]

def draw_dot(obj):
    obj.hideturtle()
    obj.penup()
    obj.speed("fastest")
    number_of_dots = 100
    obj.setheading(225)
    obj.forward(300)
    obj.setheading(0)
    for dot_count in range(1,number_of_dots+1):
        obj.dot(20,random.choice(COLORS))
        obj.forward(50)
        if dot_count % 10 == 0:
            obj.setheading(90)
            obj.forward(50)
            obj.setheading(180)
            obj.forward(500)
            obj.setheading(0)
    

if __name__ == "__main__":
    colormode(255)
    builder = Turtle()
    builder.color("black")

    screen = Screen()

    draw_dot(builder)

    screen.exitonclick()
