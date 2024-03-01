from turtle import Turtle
import random


class Food:

    def __init__(self):
        self.position = (random.randint(-280, 280), random.randint(-280, 280))
        self.pellet = Turtle("circle")
        self.pellet.color("white")
        self.pellet.shapesize(1, 1)

    def move(self):
        self.pellet.penup()
        self.position = (random.randint(-280, 280), random.randint(-280, 280))
        self.pellet.goto(self.position)

