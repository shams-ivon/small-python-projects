from turtle import Turtle

SCOREBOARD_FONT = ("Courier", 80, "normal")
LEFT_SCORE_POSITION = (-100, 150)
RIGHT_SCORE_POSITION = (100, 150)
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.updated_scoreboard()

    def increase_left_score(self):
        self.left_score += 1
        self.updated_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.goto(LEFT_SCORE_POSITION)
        self.write(self.left_score, align="center", font=SCOREBOARD_FONT)
        self.goto(RIGHT_SCORE_POSITION)
        self.write(self.right_score, align="center", font=SCOREBOARD_FONT)
