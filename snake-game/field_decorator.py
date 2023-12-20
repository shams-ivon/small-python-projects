from turtle import Turtle

LEFT_MARGIN = -270
RIGHT_MARGIN = 270
TOP_MARGIN = 250
BOTTOM_MARGIN = -250

class Field_decorator(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.draw_border()

    def draw_border(self):
        self.draw_line((LEFT_MARGIN, TOP_MARGIN), (RIGHT_MARGIN, TOP_MARGIN))
        self.draw_line((RIGHT_MARGIN, TOP_MARGIN), (RIGHT_MARGIN, BOTTOM_MARGIN))
        self.draw_line((RIGHT_MARGIN, BOTTOM_MARGIN), (LEFT_MARGIN, BOTTOM_MARGIN))
        self.draw_line((LEFT_MARGIN, BOTTOM_MARGIN), (LEFT_MARGIN, TOP_MARGIN))

    def draw_line(self, from_pos, to_pos):
        self.goto(from_pos)
        self.pendown()
        self.goto(to_pos)
        self.penup()