import time
from turtle import Screen
from day23_player import Player
from day23_car_manager import CarManager
from day23_scoreboard import Scoreboard

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    player = Player()
    scoreboard = Scoreboard()
    car = CarManager()

    screen.listen()
    screen.onkey(player.move, "Up")

    car_density = 6
    loop = 0
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        loop += 1
        
        if loop % 6 == 0:
            car.add_car()
        
        car.move()

        finish = player.has_reached_finish_line()
        if finish:
            scoreboard.score_point()
            player.reset_position()
            car.increase_movespeed(scoreboard.score)
            if car_density > 2:
                car_density -= 1
                print(car_density)

        for any_car in car.cars:
            if player.distance(any_car) < 20:
                scoreboard.game_over()
                game_is_on = False
            if any_car.xcor() < -320:
                car.cars.remove(any_car)
                
    screen.exitonclick()
