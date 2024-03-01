from turtle import Turtle


class Scoreboard:

    def __init__(self):
        self.group_scores = []
        self.score = 0
        self.create_board()

    def create_board(self):
        this_board = Turtle()
        self.group_scores.append(this_board)
        this_board.penup()
        this_board.hideturtle()
        this_board.goto(0, 270)
        this_board.pencolor("white")
        this_board.write(f"Score: {self.score}", True, "center", ("Courier", 18, "normal"))

    def add_point(self):
        self.group_scores[0].clear()
        self.group_scores.pop(0)
        t_board = Turtle()
        self.score += 1
        t_board.penup()
        t_board.hideturtle()
        t_board.goto(0, 270)
        t_board.pencolor("white")
        t_board.write(f"Score: {self.score}", True, "center", ("Verdana", 18, "normal"))
        self.group_scores.append(t_board)

