from turtle import Turtle

STARTING_POSITION = (0, -240)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 240

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
