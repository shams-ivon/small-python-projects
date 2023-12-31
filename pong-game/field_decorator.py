from turtle import Turtle

TOP_Y = 250
BOTTOM_Y = -250
MIDDLE_X = 0
LEFT_TOP = (-370, 250)
RIGHT_TOP = (370, 250)
LEFT_BOTTOM = (-370, -250)
RIGHT_BOTTOM = (370, -250)
HORIZONTAL_BORDER_SIZE = 20
VERTICAL_BORDER_SIZE = 1
ONE_DASH_SIZE = 10

class Field_decorator(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.draw_border()
        self.draw_divider()

    def draw_border(self):
        self.draw_line(LEFT_TOP, RIGHT_TOP, HORIZONTAL_BORDER_SIZE)
        self.draw_line(RIGHT_TOP, RIGHT_BOTTOM, VERTICAL_BORDER_SIZE)
        self.draw_line(RIGHT_BOTTOM, LEFT_BOTTOM, HORIZONTAL_BORDER_SIZE)
        self.draw_line(LEFT_BOTTOM, LEFT_TOP, VERTICAL_BORDER_SIZE)

    def draw_line(self, from_pos, to_pos, border_size):
        self.goto(from_pos)
        self.pensize(border_size)
        self.pendown()
        self.goto(to_pos)
        self.penup()
    
    def draw_divider(self):
        self.setheading(90)
        self.goto(MIDDLE_X, BOTTOM_Y)
        self.pensize(VERTICAL_BORDER_SIZE)
        alter = 0
        
        while self.ycor() < TOP_Y:
            
            if alter == 0:
                self.pendown()
                alter = 1
            else:
                self.penup()
                alter = 0

            self.forward(ONE_DASH_SIZE)