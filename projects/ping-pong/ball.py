import turtle


def create_ball():
    ball = turtle.Turtle()
    ball.speed(4)  # Adjusted speed
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    ball.goto(0, 0)
    return ball
