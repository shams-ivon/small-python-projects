import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from field_decorator import Field_decorator

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

field_decorator = Field_decorator()
player = Player()

field_decorator.draw_border()
screen.onkey(player.move_forward, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
