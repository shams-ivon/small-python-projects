from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-380, 250)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.write_level()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_level()

    def write_level(self):
        self.write(f"LEVEL : {self.level}", font=FONT)

    
