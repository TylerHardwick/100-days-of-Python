import turtle
from turtle import Turtle, Screen
import random

begin_race = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Choose your turtle.", prompt="Which turtle will win the race? Enter a colour: ").lower()
cash_bet = screen.textinput(title="Place your bet.", prompt="Odds on this race are 6/1. How much would you like to bet?: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -120
all_turtles = []


if bet:
    begin_race = True


for num in range(0, len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[num])
    new_turtle.penup()
    y_position += 40
    new_turtle.setposition(x=-230, y=y_position)
    all_turtles.append(new_turtle)

while begin_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            begin_race = False
            winning_colour = turtle.pencolor()
            if winning_colour == bet:
                print(f"Boom, you win! The {winning_colour} turtle is the winner!")
                print(f"You win £{int(cash_bet) * 6}!")
            else:
                print(f"Unlucky you've lost. The {winning_colour} turtle won the race.")
        steps = random.randint(0, 10)
        turtle.forward(steps)


screen.exitonclick()