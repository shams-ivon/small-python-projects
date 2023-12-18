from turtle import Turtle
FONT = ("Comic Sans MS", 30, "normal")

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-70, 250)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):

        self.write(f"Score: {self.score}", font=FONT)

    def update_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()