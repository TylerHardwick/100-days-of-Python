from turtle import Turtle
import random
class Brick(Turtle):

    def __init__(self,xcord, ycord):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=2, stretch_len=5)
        self.color(random.choice(["red","yellow", "blue", "green"]))
        self.goto(xcord,ycord)
        self.brick_x = -280


    def pop_brick(self):
        self.setx(-500)

    def move_down_brick(self, ycord):
        self.sety(ycord)
