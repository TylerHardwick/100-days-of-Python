from turtle import Screen
from puck import Puck
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BrickBreaker by Tyler")
screen.tracer(0)


puck = Puck((0,  -200))
ball = Ball()
scoreboard = Scoreboard()

brick_x = -280
bricks_list = [[], [], []]

def create_bricks():
    global bricks_list
    global brick_x
    brick_x = -280
    bricks_list = [[], [], []]
    for num in range(5):

        bricks_1 = Brick(brick_x, 270)
        bricks_list[0].append(bricks_1)

        bricks_2 = Brick(brick_x, 200)
        bricks_list[1].append(bricks_2)

        bricks_3 = Brick(brick_x, 130)
        bricks_list[2].append(bricks_3)

        brick_x += 140


def create_new_row():
    global brick_x
    brick_x = -280
    bricks_list[2] = bricks_list[1]
    bricks_list[1] = bricks_list[0]
    for bricks in bricks_list[2]:
        bricks.move_down_brick(130)
    for bricks in bricks_list[1]:
        bricks.move_down_brick(200)
    for num in range(5):
        bricks_1 = Brick(brick_x, 270)
        bricks_list[0].append(bricks_1)
        brick_x += 140



create_bricks()


screen.listen()
screen.onkey(puck.left, "Left")
screen.onkey(puck.right,"Right")

play_game = True

while play_game:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()




    #Detect collision with walls.
    if ball.ycor() >= 280:
        ball.y_bounce()

    if ball.xcor() <= -380 or ball.xcor() >=380:
        ball.x_bounce()

    #Detect collision with puck
    if ball.distance(puck) < 90 and ball.ycor() < -180:
        print(f"Distance = {ball.distance(puck)}, ball ycor = {ball.ycor()}")
        ball.y_bounce()


    #Detect  paddle miss:
    if ball.ycor() < -380:
        ball.reset_position()
        scoreboard.decrease_lives()



    #Detect collision with bricks

    for brick in bricks_list[0]:
        if ball.distance(brick) < 80 and ball.ycor() > 250:
            ball.y_bounce()
            print(f"Hit brick on row {brick.ycor()}")
            scoreboard.increase_score(150)
            brick.pop_brick()
            bricks_list[0].pop(bricks_list[0].index(brick))


    for brick in bricks_list[1]:
        if ball.distance(brick) < 80 and ball.ycor() > 180:
            ball.y_bounce()
            print(f"Hit brick on row {brick.ycor()}")
            scoreboard.increase_score(100)
            brick.pop_brick()
            bricks_list[1].pop(bricks_list[1].index(brick))

    for brick in bricks_list[2]:
        if ball.distance(brick) < 80 and ball.ycor() > 110:
            ball.y_bounce()
            print(f"Hit brick on row {brick.ycor()}")
            scoreboard.increase_score(50)
            brick.pop_brick()
            bricks_list[2].pop(bricks_list[2].index(brick))




# ----------- Check Win --------- #
    if len(bricks_list[0]) == 0 and bricks_list[0] == bricks_list[1] == bricks_list[2]:
        print("fin")

 # ----- Check if row is empty ------------- #
    if len(bricks_list[2]) == 0 or len(bricks_list[1]) == 0:
        create_new_row()


    # ------------ Check Lose ---------- #
    if scoreboard.lives == 0:
        for lists in bricks_list:
            for brick in lists:
                brick.pop_brick()
        print("Game over")
        scoreboard.reset_lives()
        create_bricks()



print(bricks_list)
print("FIN")

screen.exitonclick()