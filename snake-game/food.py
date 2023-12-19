import random
from turtle import Turtle

LOWEST_CORX = -250
LOWEST_CORY = -230
HIGHEST_CORX = 250
HIGHEST_CORY = 230

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

        rand_x = random.randint(LOWEST_CORX, HIGHEST_CORX)
        rand_y = random.randint(LOWEST_CORY, HIGHEST_CORY)
        self.goto(rand_x, rand_y)