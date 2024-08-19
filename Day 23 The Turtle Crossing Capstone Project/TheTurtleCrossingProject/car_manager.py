from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[random.randint(0, 5)])
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(320, random.randint(-250, 250))
        self.move_speed = STARTING_MOVE_DISTANCE

    def move_left(self):
        self.forward(-self.move_speed)

    def level_up(self):
        self.clear()
        self.goto(320, random.randint(-250, 250))
        if random.randint(0, 1) == 1:
            self.move_speed += MOVE_INCREMENT
