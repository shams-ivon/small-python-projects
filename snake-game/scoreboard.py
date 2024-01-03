from turtle import Turtle

SCOREBOARD_FONT = ("Courier", 30, "normal")
GAME_OVER_FONT = ("Comic Sans MS", 60, "normal")
SCOREBOARD_POSITION = (-270, 260)
# GAME_OVER_TEXT_POSITION = (-170, -20)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
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
        
        self.score = 0
        self.updated_scoreboard()

    # def game_over(self):
    #     self.penup()
    #     self.goto(GAME_OVER_TEXT_POSITION)
    #     self.color("red")
    #     self.write("GAME OVER", font=GAME_OVER_FONT)