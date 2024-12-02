from turtle import Turtle

class Puck(Turtle):

    def __init__(self, start_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=2, stretch_len=11)
        self.color("white")
        self.goto(start_cor)

    def left(self):
        new_x = self.xcor() -40
        if new_x > -320:
            self.setx(new_x)


    def right(self):
        new_x = self.xcor() +40
        if new_x < 320:
            self.setx(new_x)

