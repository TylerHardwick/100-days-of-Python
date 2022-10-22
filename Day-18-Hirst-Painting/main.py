import turtle
from turtle import Turtle, Screen
from colors import rgb_list
import random


turtle.colormode(255)
franklin = Turtle()
franklin.pensize(10)


def change_color():
    rgb = random.choice(rgb_list)
    franklin.color(rgb)


def line_of_dots():
    for _ in range(10):
        change_color()
        franklin.dot(20)
        franklin.forward(50)




x_location = -250
y_location = -200

franklin.penup()
for num in range(10):
    franklin.sety(y_location + (num * 50) )
    franklin.setx(x_location)
    line_of_dots()










screen = Screen()
screen.exitonclick()