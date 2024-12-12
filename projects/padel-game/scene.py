import turtle

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


def create_rocket(position):
    pad = turtle.Turtle()
    # TODO rocket has 0 speed
    # TODO rocket has square shape
    # TODO rocket has black color
    # TODO rocket size is 6x2
    pad.penup()
    # TODO go to (position, 0) coordinate
    return pad
