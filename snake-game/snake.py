from turtle import Turtle

class Snake:

    def __init__(self):
        
        self.snake_blocks = []
        self.snake_positions = [(0, 0), (-20, 0), (-40, 0)]

        for index in range(3):

            block = Turtle("square")
            block.color("white")
            block.penup()
            
            block.goto(self.snake_positions[index])
            self.snake_blocks.append(block)

    def move(self):
        
        snake_size = len(self.snake_blocks)

        for index in range(snake_size - 1, 0, -1):
            
            next_x = self.snake_blocks[index - 1].xcor()
            next_y = self.snake_blocks[index - 1].ycor()
            self.snake_blocks[index].goto(next_x, next_y)

        self.snake_blocks[0].forward(20)
