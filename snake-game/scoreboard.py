from turtle import Turtle

FONT = ("Comic Sans MS", 30, "normal")
LEFT_MARGIN = -270
RIGHT_MARGIN = 270
TOP_MARGIN = 250
BOTTOM_MARGIN = -250
SCOREBOARD_POSITION = (-70, 260)

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.color("white")
        self.updated_scoreboard()
        self.draw_border()

    def draw_border(self):
        
        self.draw_line((LEFT_MARGIN, TOP_MARGIN), (RIGHT_MARGIN, TOP_MARGIN))
        self.draw_line((RIGHT_MARGIN, TOP_MARGIN), (RIGHT_MARGIN, BOTTOM_MARGIN))
        self.draw_line((RIGHT_MARGIN, BOTTOM_MARGIN), (LEFT_MARGIN, BOTTOM_MARGIN))
        self.draw_line((LEFT_MARGIN, BOTTOM_MARGIN), (LEFT_MARGIN, TOP_MARGIN))
        self.goto(SCOREBOARD_POSITION)

    def draw_line(self, from_pos, to_pos):

        self.goto(from_pos)
        self.pendown()
        self.goto(to_pos)
        self.penup()


    def updated_scoreboard(self):
        self.write(f"Score: {self.score}", font=FONT)

    def update_score(self):

        self.score += 1
        self.clear()
        self.draw_border()
        self.updated_scoreboard()