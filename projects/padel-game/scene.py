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
    game_version()  # ورژن بازی
    return screen


def create_rocket(position, color):
    rocket = turtle.Turtle()
    rocket.penup()
    rocket.goto(x=position, y=50)
    rocket.pendown()
    rocket.color(color)
    rocket.begin_fill()
    rocket.circle(5, steps=360)
    rocket.goto(x=position, y=-50)
    rocket.circle(5, steps=360)
    rocket.end_fill()
    rocket.goto(x=position, y=3)
    rocket.shape('square')
    rocket.shapesize(stretch_len=0.5, stretch_wid=5)
    rocket.penup()
    return rocket


def create_ball(ball_color):
    ball = turtle.Turtle()
    ball.speed(4)
    ball.color(ball_color)
    ball.begin_fill()
    ball.circle(12, steps=360)
    ball.end_fill()
    ball.hideturtle()
    ball.penup()
    return ball


def create_lines():
    # ایجاد ترتل
    lines = turtle.Turtle()
    lines.color("#c2c2ff")
    lines.width(10)  # قطر خطوط
    # عمودی وسط
    lines.penup()
    lines.goto(x=0, y=-285)
    lines.pendown()
    lines.goto(x=0, y=295)
    # عمودی وسط راست
    lines.penup()
    lines.goto(x=250, y=-285)
    lines.pendown()
    lines.goto(x=250, y=295)
    # عمودی وسط چپ
    lines.penup()
    lines.goto(x=-250, y=-285)
    lines.pendown()
    lines.goto(x=-250, y=295)
    # افقی وسط
    lines.penup()
    lines.goto(x=-250, y=0)
    lines.pendown()
    lines.goto(x=250, y=0)
    # اضلاع دور زمین
    lines.color(black)
    # عمودی چپ
    lines.penup()
    lines.goto(x=-495, y=-285)
    lines.pendown()
    lines.goto(x=-495, y=295)
    # عمودی راست
    lines.penup()
    lines.goto(x=490, y=-285)
    lines.pendown()
    lines.goto(x=490, y=295)
    # افقی بالا
    lines.penup()
    lines.goto(x=-495, y=295)
    lines.pendown()
    lines.goto(x=490, y=295)
    # افقی پایین
    lines.penup()
    lines.goto(x=-495, y=-289)
    lines.pendown()
    lines.goto(x=490, y=-289)
    # مخفی کردن ترتل و اتمام
    lines.hideturtle()
    return lines


def game_version():
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(420, -280)
    writer.pendown()
    writer.color("lightgrey")
    writer.write("version 1.0.0",
                 font="Bahnschrift_Light", align="center")
    writer.hideturtle()
    return writer
