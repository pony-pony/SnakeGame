from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color('yellow')
        self.speed(0)
        random_x = 20 * random.randint(-14, 14)
        random_y = 20 * random.randint(-14, 14)
        self.goto(random_x, random_y)
        # self.refresh()

    def refresh(self):
        random_x = 20 * random.randint(-14, 14)
        random_y = 20 * random.randint(-14, 14)
        self.goto(random_x, random_y)