from turtle import Turtle
import random
from SnakeBody import Snake

dice_locx = [pos for pos in range(-280, 280, 20)]
dice_locy = []
dice_locy.extend(dice_locx)


class Dice:

    def __init__(self):
        self.pos = (random.choice(dice_locx), random.choice(dice_locy))
        self.new_dice = Turtle("circle")
        self.new_dice.color("blue")
        self.new_dice.penup()
        self.new_dice.goto(self.pos)
        self.point = 0

    def dice_pos_check(self, snake):
        flag = 0
        # if (Snake.head.xcor() == self.new_dice.xcor() and Snake.head.ycor() == self.new_dice.ycor()) \
        #         or ((Snake.head.xcor()+1) == self.new_dice.xcor() and Snake.head.ycor() == self.new_dice.ycor()) \
        #         or (Snake.head.xcor() == self.new_dice.xcor() and (Snake.head.ycor()+1) == self.new_dice.ycor()) \
        #         or ((Snake.head.xcor()+1) == self.new_dice.xcor() and (Snake.head.ycor()+1) == self.new_dice.ycor()):
        if (snake.head.xcor() == self.new_dice.xcor() or snake.head.xcor() + 1 == self.new_dice.xcor()) and (snake.head.ycor() == self.new_dice.ycor() or snake.head.ycor() + 1 == self.new_dice.ycor()):
            snake.add_new_block()
            while True:
                self.pos = (random.choice(dice_locx), random.choice(dice_locy))
                self.new_dice.penup()
                for i in range(len(snake.snakebody)):
                    if self.pos[0] == snake.snakebody[i].xcor() and self.pos[1] == snake.snakebody[i].ycor():
                        break
                    else:
                        flag = 1
                        continue
                if flag == 1:
                    self.new_dice.goto(self.pos)
                    self.point += 1
                    print(f"dice {self.new_dice.pos()}")
                    break
