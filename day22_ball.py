from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce(self,direction):
        if direction == "y":
            self.y_move *= -1
            self.move_speed *= 0.85
        else:
            self.x_move *= -1
            self.move_speed *= 0.85
        
    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce("x")