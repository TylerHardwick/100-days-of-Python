from turtle import Turtle



class Puck(Turtle):

    def __init__(self, start_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(start_cor)

    def up(self):
        new_y = self.ycor() +20
        if new_y < 260:
            self.sety(new_y)

    def down(self):
        new_y = self.ycor() -20
        if new_y > -260:
            self.sety(new_y)








