import turtle

# Create scence elements: Screen, Ball, Paddles

# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.title
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.bgcolor
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.setup
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.shape
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.color
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.goto
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.speed
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.shapesize


def create_screen(width, height):
    screen = turtle.Screen()  # initiate a screen using turtle library
    # TODO add game title
    # TODO add background color
    # TODO setup width and height
    return screen


def create_ball():
    ball = turtle.Turtle()
    ball.speed(4)  # Adjusted speed
    # TODO create a circle shape
    # TODO add ball color
    ball.penup()
    # TODO go to (0, 0) coordinate
    return ball


def create_paddle(position):
    pad = turtle.Turtle()
    # TODO paddle has 0 speed
    # TODO paddle has square shape
    # TODO paddle has black color
    # TODO paddle size is 6x2
    pad.penup()
    # TODO go to (position, 0) coordinate
    return pad
