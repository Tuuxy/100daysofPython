from turtle import Screen
from day22_paddle import Paddle
from day22_ball import Ball
from day22_scoreboard import Scoreboard
import time


if __name__ == "__main__":

    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800,height=600)
    screen.title("Pong")
    screen.tracer(0)
    
    r_paddle = Paddle((350,0))
    l_paddle = Paddle((-350,0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "q")
    screen.onkey(l_paddle.go_down, "d")
    
    screen.listen()

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce("y")
        
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce("x")

        if ball.xcor() > 400:
            ball.reset_position()
            scoreboard.l_point()

        if ball.xcor() < -400:
            ball.reset_position()
            scoreboard.r_point()

    screen.exitonclick()