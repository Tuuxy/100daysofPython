from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)
        self.color("white")
    
    def go_up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)
    
    def go_down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)
