from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            new_location = car.xcor() - self.car_speed
            car.setx(new_location)

    def spawn_car(self):
        spawn_chance = random.randint(1, 6)
        if spawn_chance > 5:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len= 2)
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT





