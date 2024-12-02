from turtle import Turtle

FONT = ("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.penup()
        self.hideturtle()
        self.color("grey")
        self.display_score()


    def display_score(self):
        self.clear()
        self.goto(x=-390, y=-290)
        self.write(arg=f"Score:{self.score}",font=FONT ,align="left")
        self.goto(x=250, y=-290)
        self.write(arg=f"Lives:{self.lives}",font=FONT ,align="left")


    def increase_score(self, points):
        self.score += points
        self.display_score()

    def decrease_lives(self):
        self.lives -= 1
        self.display_score()

    def reset_lives(self):
        self.score = 0
        self.lives += 3
        self.display_score()