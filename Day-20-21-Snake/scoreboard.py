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
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score}    High Score: {self.high_score}", align= ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.current_score = 0
        self.update_score()

    def increase_score(self):
        self.current_score +=1
        self.update_score()