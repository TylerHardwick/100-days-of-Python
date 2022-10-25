from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Tyler's Snake Game")
screen.tracer(0)



food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

play_game = True
while play_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.eaten_move()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        play_game = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            play_game = False
            scoreboard.game_over()





screen.exitonclick()