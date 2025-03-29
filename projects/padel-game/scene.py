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
    create_lines()  # رسمو خطوط
    paddle_game()  # نوشته پس زمنیه
    game_version()  # ورژن بازی
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
    lines.color('#c2c2ff')
    lines.width(5)  # قطر خطوط
    # خط عمودی وسط
    lines.penup()  # چیزی نکش
    lines.goto(x=0, y=-300)  # از
    lines.pendown()  # شروع کن به کشیدن
    lines.goto(x=0, y=300)  # تا
    # خط عمودی راست
    lines.penup()  # چیزی نکش
    lines.goto(x=491, y=-300)  # از
    lines.pendown()  # شروع کن به کشیدن
    lines.goto(x=491, y=300)  # تا
    # خط عمودی راست
    # TODO
    # خط افقی بالا
    # TODO
    # خط افقی پایین
    # TODO
    lines.hideturtle()
    return lines


def game_version():
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(420, -280)
    writer.pendown()
    writer.color("Gray20")
    writer.write("version 1.0.0",
                 font="Bahnschrift_Light", align="center")
    writer.hideturtle()
    return writer


def paddle_game():
    txt = turtle.Turtle()
    txt.penup()
    txt.goto(0, 0)
    txt.pendown()
    txt.color("Gray20")
    txt.write("Paddle Game", font="shabnam", align="center")
    txt.hideturtle()
    return txt
