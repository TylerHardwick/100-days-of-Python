import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Tyler the Turtle, Crossy-Road")
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")

player.player_start()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move()

    # Detect collision with Car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with Wall
    if player.ycor() >= player.finish:
        player.finish_level()
        scoreboard.next_level()
        car_manager.increase_car_speed()

screen.exitonclick()

