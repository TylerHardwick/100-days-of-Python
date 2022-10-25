from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.print_level()

    def print_level(self):
        self.clear()
        self.goto(x=-280,y=260)
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(arg="Game Over... GG", font=FONT, align="center")

    def next_level(self):
        self.level +=1
        self.print_level()


