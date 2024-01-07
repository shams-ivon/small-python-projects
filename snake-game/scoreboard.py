from turtle import Turtle

SCOREBOARD_FONT = ("Courier", 30, "normal")
SCOREBOARD_POSITION = (-270, 260)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.set_high_score_from_file()
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.color("white")
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}        High Score:{self.high_score}", font=SCOREBOARD_FONT)

    def update_score(self):
        self.score += 1
        self.updated_scoreboard()

    def reset_score(self):

        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score_into_file() 
        
        self.score = 0
        self.updated_scoreboard()

    def set_high_score_from_file(self):

        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        
    def set_high_score_into_file(self):

        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))