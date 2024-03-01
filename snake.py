from turtle import Turtle
from food import Food
import math

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        self.segments = []
        self.counter = 1
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed(self.counter)
            new_segment.goto(position)
            self.segments.append(new_segment)

    def create_snake_piece(self):
        new_piece = Turtle("square")
        new_piece.color("white")
        new_piece.penup()
        new_piece.speed(self.counter)
        new_piece.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_piece)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def speed_up(self):
        if len(self.segments) >= 10 and len(self.segments) < 20:
            self.counter = 3
            """for segment in self.segments:
                segment.speed(self.counter)"""
        if len(self.segments) >= 20 and len(self.segments) < 30:
            self.counter = 6
            """for segment in self.segments:
                segment.speed(self.counter)"""
        if len(self.segments) >= 30 and len(self.segments) < 40:
            self.counter = 10
            """for segment in self.segments:
                segment.speed(self.counter)"""
        if len(self.segments) >= 40:
            self.counter = 0
            """for segment in self.segments:
                segment.speed(self.counter)"""

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(0)

