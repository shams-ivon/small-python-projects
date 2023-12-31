from turtle import Turtle

CHANGE_COORDINATE = 15
SLEEP_TIME = 0.15

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.change_xcor = CHANGE_COORDINATE
        self.change_ycor = CHANGE_COORDINATE
        self.sleep_time = SLEEP_TIME
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.penup()

    def move(self):
        new_xcor = self.xcor() + self.change_xcor
        new_ycor = self.ycor() + self.change_ycor
        self.goto(new_xcor, new_ycor)

    def reverse_change_xcor(self):
        self.change_xcor = -self.change_xcor

    def reverse_change_ycor(self):
        self.change_ycor = -self.change_ycor
