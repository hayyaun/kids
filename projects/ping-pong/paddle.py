import turtle


def create_paddle(position):
    pad = turtle.Turtle()
    pad.speed(0)
    pad.shape("square")
    pad.color("black")
    pad.shapesize(stretch_wid=6, stretch_len=2)
    pad.penup()
    pad.goto(position, 0)
    return pad
