from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        self.cars = []
        self.movespeed = STARTING_MOVE_DISTANCE

    
    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1,2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.goto(300,random.randint(-230,230))
        self.cars.append(new_car)
    
    def move(self):
        for car in self.cars:
            car.forward(self.movespeed)
    
    def increase_movespeed(self,score):
        if self.movespeed < 85:
            self.movespeed += score * MOVE_INCREMENT
    