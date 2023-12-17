from turtle import Turtle

SNAKE_STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
ONE_MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        
        self.snake_blocks = []
        self.create_snake()

    def create_snake(self):

        for index in range(3):

            block = Turtle("square")
            block.color("white")
            block.penup()
            
            block.goto(SNAKE_STARTING_POSITION[index])
            self.snake_blocks.append(block)

    def move(self):
        
        snake_size = len(self.snake_blocks)

        for index in range(snake_size - 1, 0, -1):
            
            next_x = self.snake_blocks[index - 1].xcor()
            next_y = self.snake_blocks[index - 1].ycor()
            self.snake_blocks[index].goto(next_x, next_y)

        self.snake_blocks[0].forward(ONE_MOVE_DISTANCE)

    def up(self):

        self.snake_blocks[0].setheading(90)

    def down(self):

        self.snake_blocks[0].setheading(270)

    def left(self):

        self.snake_blocks[0].setheading(180)

    def right(self):

        self.snake_blocks[0].setheading(0)
