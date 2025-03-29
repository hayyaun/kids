import turtle
from colors import *

# Create scence elements: Screen, Ball, Rockets

# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.title
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.bgcolor
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.setup
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.shape
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.color
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.goto
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.speed
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.shapesize


def create_screen(width, height):
    screen = turtle.Screen()
    screen.title("Paddle Game")
    screen.bgcolor(bg_color)
    screen.setup(width=width, height=height)
    screen.tracer(0)
    return screen


def create_rocket(position, color):
    rocket = turtle.Turtle()
    rocket.speed(0)
    rocket.shape("square")
    rocket.color(color)
    rocket.shapesize(stretch_wid=5, stretch_len=0.5)
    rocket.penup()
    rocket.goto(x=position, y=0)
    return rocket


def create_ball(ball_color):
    ball = turtle.Turtle()
    ball.speed(4)
    ball.shape("circle")
    ball.color(ball_color)
    ball.penup()
    return ball


def create_lines():
    lines = turtle.Turtle()

    # TODO

    return lines
