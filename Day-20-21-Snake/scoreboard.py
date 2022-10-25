from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(260)
        self.current_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Current Score: {self.current_score}", align= ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over... GG", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score +=1
        self.update_score()