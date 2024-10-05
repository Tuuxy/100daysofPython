from turtle import Turtle, Screen
import random
import tkinter as tk
from tkinter import messagebox

def initiate_turtles(turtle_list,COLORS):
    for color in COLORS:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        turtle_list.append(new_turtle)

def place_turtles(turtle_list,x,y):
    for index, turtle in enumerate(turtle_list):
        turtle.penup()
        turtle.goto(x,y + (index*50))

def race_on(turtle_list):
    is_race_on = True
    while is_race_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    display_win(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    display_win(f"You've lost! The {winning_color} turtle is the winner!")
                is_race_on = False    
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)

def display_win(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Race result",message)
    root.destroy()


if __name__ == "__main__":
    COLORS = ["red","orange","yellow","green","blue","purple"]
    x = -230
    y = -125

    screen = Screen()
    screen.setup(width=500,height=400)

    user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? (red,orange,yellow,green,blue,purple): ")

    turtles = []
    initiate_turtles(turtles,COLORS)
    place_turtles(turtles,x,y)

    if user_bet:
        race_on(turtles)
    
    screen.exitonclick()