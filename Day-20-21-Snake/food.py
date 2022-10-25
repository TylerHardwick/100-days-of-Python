from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len= 0.5)
        self.color("green")
        self.eaten_move()


    def eaten_move(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(x= random_x, y= random_y)