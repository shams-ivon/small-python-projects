import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STRETCH_VER = 1
STRETCH_HOR = 2
FROM_Y = -200
TO_Y = 200
X_COR = 380
CAR_SPEED = 10
CAR_VERTICAL_DISTANCE = 10
SPEED_UP = 10

class Car_manager:
    
    def __init__(self):
        self.cars = []
        self.car_speed = CAR_SPEED

    def one_move(self):
        self.create_car()
        self.move_all_cars_one_step_forward()

    def create_car(self):
        car = Turtle()
        car.penup()
        car.color(COLORS[random.randint(0, len(COLORS) - 1)])
        car.shape("square")
        car.speed(0)
        car.shapesize(stretch_len=STRETCH_HOR, stretch_wid=STRETCH_VER)
        car.goto(X_COR, random.randint(FROM_Y, TO_Y))
        self.cars.append(car)

    def move_all_cars_one_step_forward(self):

        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += SPEED_UP

