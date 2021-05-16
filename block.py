from turtle import Turtle
import random

class Block(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'orange', 'purple']
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(xpos, ypos)
        self.color(random.choice(self.colors))
        self.blocks = []
