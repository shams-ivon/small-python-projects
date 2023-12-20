from turtle import Turtle

STRETCH_HOR = 1.5
STRETCH_VER = 4.5
TOP_MARGIN = 200
BOTTOM_MARGIN = -200

class Paddle(Turtle):

    def __init__(self, goto_x, goto_y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=STRETCH_HOR, stretch_wid=STRETCH_VER)
        self.goto(goto_x, goto_y)

    def up(self):
        move_up = min([100, TOP_MARGIN - self.ycor()])
        cur_x = self.xcor()
        cur_y = self.ycor()
        self.goto(cur_x, cur_y + move_up)
    
    def down(self):
        move_down = min([100, self.ycor() - BOTTOM_MARGIN])
        cur_x = self.xcor()
        cur_y = self.ycor()
        self.goto(cur_x, cur_y - move_down)
