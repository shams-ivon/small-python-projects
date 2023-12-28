from turtle import Turtle

LEFT_TOP = (-270, 250)
RIGHT_TOP = (270, 250)
LEFT_BOTTOM = (-270, -250)
RIGHT_BOTTOM = (270, -250)

class Field_decorator(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.draw_border()

    def draw_border(self):
        self.draw_line(LEFT_TOP, RIGHT_TOP)
        self.draw_line(RIGHT_TOP, RIGHT_BOTTOM)
        self.draw_line(RIGHT_BOTTOM, LEFT_BOTTOM)
        self.draw_line(LEFT_BOTTOM, LEFT_TOP)

    def draw_line(self, from_pos, to_pos):
        self.goto(from_pos)
        self.pendown()
        self.goto(to_pos)
        self.penup()