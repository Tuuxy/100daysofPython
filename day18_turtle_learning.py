# This code is a little weird, it was just a Turtle library training, don't mind it.

from turtle import Turtle, Screen, colormode, clearscreen
from random import choice, randint


def spirograph(obj,size_of_gap):
    random_pos(obj)
    obj.speed("fastest")
    obj.width(2)
    for _ in range(int(360 / size_of_gap)):
        obj.color(random_color())
        obj.circle(100)
        current_heading = obj.heading()
        obj.setheading(current_heading+size_of_gap)

def random_pos(obj):
    x = randint(-1000,1000)
    y = randint(-250,250)
    obj.setpos(x,y)

def random_color():
    colormode(255)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    return color

def draw_shapes(obj,num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        obj.forward(100)
        obj.left(angle)

def drawing_shapes(obj,shapes):
    random_pos(obj)
    obj.speed("fast")
    obj.width(5)
    for shape in shapes:
        draw_shapes(obj,shape)
        obj.color(random_color())

def random_walk(obj):
    random_pos(obj)
    obj.speed("fastest")
    obj.width(4)
    moves = [obj.left,obj.right,obj.forward]
    for _ in range(3000):
        obj.color(random_color())
        move = choice(moves)
        
        if move == obj.forward:
            move(10)
        else:
            move(90)

if __name__ == "__main__":
    himothy = Turtle(shape="turtle")
    timmy = Turtle(shape="turtle")
    franklin = Turtle(shape="turtle")
    
    shapes = [i for i in range(3,15)]

    screen = Screen()
    screen.bgcolor("black")
    
    spirograph(himothy,5)
    drawing_shapes(timmy,shapes)
    random_walk(franklin)

    screen.exitonclick()