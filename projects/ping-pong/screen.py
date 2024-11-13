import turtle


def create_screen(width, height):
    screen = turtle.Screen()  # initiate a screen using turtle library
    screen.title("Pong game")  # add game title
    screen.bgcolor("white")  # add background color
    screen.setup(width, height)  # setup width and height
    return screen
