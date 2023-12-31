from turtle import Turtle

SNAKE_STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
ONE_MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.create_snake_and_set_head()

    def create_snake_and_set_head(self):
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):

        for position in SNAKE_STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.snake_blocks.append(block)

    def extend_snake(self):
        self.add_segment(self.snake_blocks[-1].position())

    def move(self):
        snake_size = len(self.snake_blocks)

        for index in range(snake_size - 1, 0, -1):
            next_x = self.snake_blocks[index - 1].xcor()
            next_y = self.snake_blocks[index - 1].ycor()
            self.snake_blocks[index].goto(next_x, next_y)

        self.head.forward(ONE_MOVE_DISTANCE)

    def reset(self):

        for block in self.snake_blocks:
            block.hideturtle()

        self.snake_blocks.clear()
        self.create_snake_and_set_head()

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
