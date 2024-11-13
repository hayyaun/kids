import turtle

# Create scence elements: Screen, Ball, Paddles


def create_screen(width, height):
    screen = turtle.Screen()  # initiate a screen using turtle library
    screen.title("Pong game")  # TODO add game title
    screen.bgcolor("white")  # TODO add background color
    screen.setup(width, height)  # TODO setup width and height
    return screen


def create_ball():
    ball = turtle.Turtle()
    ball.speed(4)  # Adjusted speed
    ball.shape("circle")  # TODO create a circle shape
    ball.color("blue")  # TODO add ball color
    ball.penup()
    ball.goto(0, 0)  # TODO go to (0, 0) coordinate
    return ball


def create_paddle(position):
    pad = turtle.Turtle()
    pad.speed(0)  # TODO paddle has 0 speed
    pad.shape("square")  # TODO paddle has square shape
    pad.color("black")  # TODO paddle has black color
    pad.shapesize(stretch_wid=6, stretch_len=2)  # TODO paddle size is 6x2
    pad.penup()
    pad.goto(position, 0)  # TODO go to (position, 0) coordinate
    return pad
