from turtle import Turtle
import sys

intial_co = ((0, 0), (-20, 0), (-40, 0))
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0
MOVE_DIST = 20


class Snake:

    def __init__(self):
        self.snakebody = []
        new_block = Turtle("square")
        new_block.color("red")
        new_block.penup()
        new_block.goto(intial_co[0])
        new_block.setheading(EAST)
        self.snakebody.append(new_block)
        self.creating_snake_body()
        self.head = self.snakebody[0]

    def creating_snake_body(self):
        for i in range(len(intial_co) - 1):
            new_block = Turtle("square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(intial_co[i])
            new_block.setheading(EAST)
            self.snakebody.append(new_block)

    def snake_movement(self):

        for i in range(len(self.snakebody) - 1, 0, -1):
            x = int(self.snakebody[i - 1].xcor())
            y = int(self.snakebody[i - 1].ycor())
            self.snakebody[i].goto(x, y)
        self.head.forward(MOVE_DIST)
        print(f"snake {x}, {y}")

    def snake_heading_left(self):
        if self.head.heading() == NORTH:
            self.head.setheading(WEST)
        elif self.head.heading() == WEST:
            self.head.setheading(SOUTH)
        elif self.head.heading() == SOUTH:
            self.head.setheading(EAST)
        elif self.head.heading() == EAST:
            self.head.setheading(NORTH)


    def snake_heading_right(self):
        if self.head.heading() == NORTH:
            self.head.setheading(EAST)
        elif self.head.heading() == EAST:
            self.head.setheading(SOUTH)
        elif self.head.heading() == SOUTH:
            self.head.setheading(WEST)
        elif self.head.heading() == WEST:
            self.head.setheading(NORTH)


    def border_check(self):
        if int(self.head.xcor()) >= 300:
            sys.exit()
        elif int(self.head.xcor()) <= -300:
            sys.exit()
        elif int(self.head.ycor()) <= -300:
            sys.exit()
        elif int(self.head.ycor()) >= 300:
            sys.exit()

    def add_new_block(self):
        new_block = Turtle("square")
        new_block.penup()
        new_block.color("white")
        new_block.goto(self.snakebody[-1].xcor(), self.snakebody[-1].ycor())
        new_block.setheading(self.snakebody[-1].heading())
        self.snakebody.append(new_block)

    def on_body_collision(self):
        for i in range(1, len(self.snakebody)):
            if self.head.xcor() == self.snakebody[i].xcor() \
                    and self.head.ycor() == self.snakebody[i].ycor():
                sys.exit()
