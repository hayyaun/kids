

# Functions to move rocket


def rocket_up(pad):
    y = pad.ycor()
    if y < 250:  # check if rocket y is less than 250
        # TODO then move pad up +20 and set y
        print("rocket up")


def rocket_down(pad):
    y = pad.ycor()
    if y > -240:  # check if rocket y is bigger than -240
        # TODO then move pad down -20 and set y
        print("rocket down")


# Create Keyboard Bindings to move rockets


def add_keyboard_bindings(screen, left_pad, right_pad):

    def rocket_left_up(): return rocket_up(left_pad)
    def rocket_left_down(): return rocket_down(left_pad)
    def rocket_right_up(): return rocket_up(right_pad)
    def rocket_right_down(): return rocket_down(right_pad)

    # Hint: You can check documentations: https://docs.python.org/3/library/turtle.html#turtle.onkeypress

    screen.listen()
    # TODO listen for key 'w' and call rocket_left_up
    # TODO listen for key 's' and call rocket_left_down
    # TODO listen for key 'Up' and call rocket_right_up
    # TODO listen for key 'Down' and call rocket_right_up
