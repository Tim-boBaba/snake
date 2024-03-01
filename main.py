from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True

#Create a snake body
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

pellet = Food()
pellet.move()

board = Scoreboard()


def is_collided(a, b):
    distance = b.distance(a.pos())
    radius_a = a.shapesize()[0] * 10
    radius_b = b.shapesize()[0] * 10
    return radius_a + radius_b >= distance


#Move the snake
while game_is_on:
    screen.update()
    if snake.counter == 1:
        time.sleep(0.1)
    elif snake.counter == 3:
        time.sleep(0.08)
    elif snake.counter == 6:
        time.sleep(0.06)
    elif snake.counter == 10:
        time.sleep(0.04)
    elif snake.counter == 0:
        time.sleep(0.02)

    snake.move()
    if is_collided(snake.head, pellet.pellet):
        pellet.move()
        board.add_point()
        snake.create_snake_piece()
        snake.speed_up()
        screen.update()

    for segment in snake.segments:
        if segment == snake.head:
            continue
        if snake.head.distance(segment) <= 5:
            game_is_on = False

    if snake.head.xcor() >= 290 or snake.head.ycor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() <= -290:
        game_is_on = False

if not game_is_on:
    print(f"Game Over. Your final score: {board.score}")
    #Debugging print for snake's speed
    #print(f"Snake head speed: {snake.head.speed()}")

screen.exitonclick()
