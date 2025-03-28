import turtle
from colors import *


def create_score_board(left_score, right_score):
    # Create score board
    score_board = turtle.Turtle()

    # Create main box
    draw_colored_box(score_board, black, -137, 263, 250, 27)  # main box
    draw_colored_box(score_board, bg_color, -54, 263, 3, 27)  # Left color box
    draw_colored_box(score_board, bg_color, 18, 263, 3, 27)  # Right color box
    create_triangle(score_board, -153)  # Left triangle
    create_triangle(score_board, 99)  # Right triangle

    # Write texts
    writeTexts(score_board)

    # Left player lights
    for i in range(5):
        light_color = white
        if left_score > i:
            light_color = player_left_color
        draw_circle(score_board, light_color, -105 + 10*i)

    # Right player lights
    for i in range(5):
        light_color = white
        if right_score > i:
            light_color = player_right_color
        draw_circle(score_board, light_color, 75 - 10*i)

    turtle.hideturtle()
    return score_board


def show_scores(score_board, left_score, right_score):
    # Clear & Show scores of each player again
    score_board.clear()
    create_score_board(left_score, right_score)


# NIKAN


def create_triangle(t: turtle.Turtle, x):
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


def draw_colored_box(t: turtle.Turtle, color, x0, y0, width, height):
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


def writeTexts(t: turtle.Turtle):
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


def draw_circle(t: turtle.Turtle, color, x):
    t.speed(100)
    t.penup()
    t.goto(x, 266)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.hideturtle()
