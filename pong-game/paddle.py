from turtle import Turtle

STRETCH_HOR = 1.5
STRETCH_VER = 4.5
TOP_MARGIN = 200
BOTTOM_MARGIN = -200
ONE_VERTICAL_MOVE = 20

class Paddle(Turtle):

    def __init__(self, goto_x, goto_y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=STRETCH_HOR, stretch_wid=STRETCH_VER)
        self.goto(goto_x, goto_y)

    def up(self):
        cur_x = self.xcor()
        cur_y = self.ycor()
        move_up = min([ONE_VERTICAL_MOVE, TOP_MARGIN - cur_y])
        self.goto(cur_x, cur_y + move_up)
    
    def down(self):
        cur_x = self.xcor()
        cur_y = self.ycor()
        move_down = min([ONE_VERTICAL_MOVE, cur_y - BOTTOM_MARGIN])
        self.goto(cur_x, cur_y - move_down)
