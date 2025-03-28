import turtle
from colors import *

# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.color
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.goto
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.speed
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.write


def create_score_board():
    # Create score board
    score_board = turtle.Turtle()
    # TODO scoreboard has 0 speed
    # TODO add color to scoreboard
    score_board.penup()
    score_board.hideturtle()
    # TODO move scoreboard to (0, 260) coordinate
    return score_board


def show_scores(score_board):
    # Show scores of each player
    score_board.clear()
    left_score = score_board.left_player
    right_score = score_board.right_player
    scores = f"Left: {left_score}       Right: {right_score}"
    # TODO write scores, aligned at center, with a good font


# NIKAN

black = "#41444B"
white = "#FFFAF0"
orange = "#FFB26F"
blue = "#8F87F1"
green = "#00FF00"


def create_triangle(x):
    t = turtle.Turtle()
    t.speed(100)
    t.color(black)
    t.penup()
    t.goto(x, 290)
    t.pendown()
    t.begin_fill()

    for _ in range(3):
        t.forward(30)
        t.left(-120)

    t.end_fill()
    t.hideturtle()


def draw_colored_box(color, x0, y0, width, height):
    t = turtle.Turtle()
    t.speed(100)
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.color(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()
    t.hideturtle()


def writeTexts():
    t = turtle.Turtle()

    t.penup()
    t.goto(-45, 274)
    t.pendown()
    t.color(white)
    t.write("PADEL", font=("Lucida Handwriting", 7, "bold"))

    t.penup()
    t.goto(-20, 268)
    t.pendown()
    t.color(white)
    t.write("GAMES", font=("Algerian", 7, "bold"))

    t.penup()
    t.goto(-112, 273)
    t.pendown()
    t.color(player_left_color)
    t.write("PLAYER 1", font=("Arial", 8, "bold"))
    t.hideturtle()

    t.penup()
    t.goto(34, 273)
    t.pendown()
    t.color(player_right_color)
    t.write("PLAYER 2", font=("Arial", 8, "bold"))
    t.hideturtle()


def draw_circle(color, x):
    t = turtle.Turtle()
    t.speed(100)
    t.penup()
    t.goto(x, 266)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.hideturtle()
