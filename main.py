from turtle import Screen
from SnakeBody import Snake
from DicePosition import Dice
import time
from tkinter import messagebox

screen = Screen()
screen.setup(width=602, height=602)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(1)
game_on = True


Mysnake = Snake()
MyDice = Dice()

screen.listen()
screen.onkey(Mysnake.snake_heading_left, "Left")
screen.onkey(Mysnake.snake_heading_right, "Right")
screen.tracer(0)
while game_on:
    screen.update()
    time.sleep(0.1)
    Mysnake.snake_movement()
    Mysnake.border_check()
    MyDice.dice_pos_check(Mysnake)
    Mysnake.on_body_collision()

messagebox.showinfo("Result", f"Score is {MyDice.point}")
screen.exitonclick()
