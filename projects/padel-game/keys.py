import turtle


# Functions to move rocket


def rocket_up(rocket: turtle.Turtle):
    y = rocket.ycor()  # موقعیت عمودی راکت
    # اگه راکت انقد از صفحه بالا رفت که خارج داشت میشد
    if y > 250:
        return  # stop

    # move rocket up +20 and set y
    # TODO


def rocket_down(rocket: turtle.Turtle):
    y = rocket.ycor()  # موقعیت عمودی راکت
    # اگه راکت انقد از صفحه پایین رفت که خارج داشت میشد
    if y < -240:
        return  # stop

    # move rocket down -20 and set y
    # TODO


# Create Keyboard Bindings to move rockets


def add_keyboard_bindings(screen, left_rocket, right_rocket):

    def rocket_left_up(): return rocket_up(left_rocket)
    def rocket_left_down(): return rocket_down(left_rocket)
    def rocket_right_up(): return rocket_up(right_rocket)
    def rocket_right_down(): return rocket_down(right_rocket)

    # Hint: You can check documentations: https://docs.python.org/3/library/turtle.html#turtle.onkeypress

    screen.listen()
    # به ازای فشار داده شدن هر کلید زیر تابع مربوط بهش رو صدا کن
    # key 'w' -> call rocket_left_up
    # TODO
    # key 's' -> call rocket_left_down
    # TODO
    # key 'Up' -> call rocket_right_up
    # TODO
    # key 'Down' -> call rocket_right_up
    # TODO
