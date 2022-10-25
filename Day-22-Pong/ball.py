from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
            new_x = self.xcor() + self.xmove
            new_y = self.ycor() + self.ymove
            self.goto(new_x, new_y)

    def y_bounce(self):
        self.ymove *= -1

    def x_bounce(self):
        self.xmove *= -1
        self.move_speed *= 0.9
        print(self.move_speed)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()





