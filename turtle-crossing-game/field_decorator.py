from turtle import Turtle

LEFT_TOP = (-400, 250)
RIGHT_TOP = (400, 250)
LEFT_BOTTOM = (-400, -250)
RIGHT_BOTTOM = (400, -250)

class Field_decorator(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.draw_border()

    def draw_border(self):
        self.draw_line(LEFT_TOP, RIGHT_TOP)
        self.draw_line(RIGHT_BOTTOM, LEFT_BOTTOM)

    def draw_line(self, from_pos, to_pos):
        self.goto(from_pos)
        self.pendown()
        self.goto(to_pos)
        self.penup()