from turtle import Screen
from puck import Puck
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong by Tyler")
screen.tracer(0)

r_puck = Puck((350,  0))
l_puck = Puck((-350,  0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_puck.up, "w")
screen.onkey(l_puck.down, "s")
screen.onkey(r_puck.up, "Up")
screen.onkey(r_puck.down, "Down")



play_game = True
while play_game:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    #Detect collision with walls.
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()

    #Detect collision with pucks.
    if ball.distance(r_puck) < 50 and ball.xcor() > 320 or ball.distance(l_puck) < 50 and ball.xcor() < -320:
        ball.x_bounce()



    #Detect R paddle miss:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






















screen.exitonclick()

