import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("red")
        self.speed(0)
        self.new_food_appears()

    def new_food_appears(self):

        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)