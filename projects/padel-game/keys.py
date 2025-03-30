import turtle
from turtle import _Screen

# Functions to move rocket


def rocket_left(rocket, limit):
    x = rocket.xcor()
    if x < limit:
        return
    rocket.setx(x - 20)


def rocket_right(rocket, limit):
    x = rocket.xcor()

    if x > limit:
        return
    rocket.setx(x + 20)


def rocket_up(rocket: turtle.Turtle):
    y = rocket.ycor()  # موقعیت عمودی راکت
    # اگه راکت انقد از صفحه بالا رفت که خارج داشت میشد
    if y > 220:
        return  # stop

    # move rocket up +20 and set y
    rocket.sety(y + 32)


def rocket_down(rocket: turtle.Turtle):
    y = rocket.ycor()  # موقعیت عمودی راکت
    # اگه راکت انقد از صفحه پایین رفت که خارج داشت میشد
    if y < -220:
        return  # stop

    # move rocket down -20 and set y
    rocket.sety(y - 32)


# Create Keyboard Bindings to move rockets


def add_keyboard_bindings(screen: _Screen, left_rocket: turtle.Turtle, right_rocket: turtle.Turtle):

    def rocket_right_left(): return rocket_left(right_rocket, 420)
    def rocket_right_right(): return rocket_right(right_rocket, 455)
    def rocket_left_left(): return rocket_left(left_rocket, -475)
    def rocket_left_right(): return rocket_right(left_rocket, -425)
    def rocket_left_up(): return rocket_up(left_rocket)
    def rocket_left_down(): return rocket_down(left_rocket)
    def rocket_right_up(): return rocket_up(right_rocket)
    def rocket_right_down(): return rocket_down(right_rocket)

    # Hint: You can check documentations: https://docs.python.org/3/library/turtle.html#turtle.onkeypress
    screen.listen()
    # به ازای فشار داده شدن هر کلید زیر تابع مربوط بهش رو صدا کن
    # Left player
    screen.onkeypress(rocket_left_up, "w")
    screen.onkeypress(rocket_left_up, "W")
    screen.onkeypress(rocket_left_down, "s")
    screen.onkeypress(rocket_left_down, "S")
    screen.onkeypress(rocket_left_right, "d")
    screen.onkeypress(rocket_left_right, "D")
    screen.onkeypress(rocket_left_left, "a")
    screen.onkeypress(rocket_left_left, "A")
    # Right Player
    screen.onkeypress(rocket_right_up, "Up")
    screen.onkeypress(rocket_right_right, "Right")
    screen.onkeypress(rocket_right_down, "Down")
    screen.onkeypress(rocket_right_left, "Left")
