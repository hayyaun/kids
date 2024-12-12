

# Functions to move paddle


def paddle_up(pad):
    y = pad.ycor()
    if y < 250:  # check if paddle y is less than 250
        # TODO then move pad up +20 and set y
        print("paddle up")


def paddle_down(pad):
    y = pad.ycor()
    if y > -240:  # check if paddle y is bigger than -240
        # TODO then move pad down -20 and set y
        print("paddle down")


# Create Keyboard Bindings to move paddles


def add_keyboard_bindings(screen, left_pad, right_pad):

    def paddle_left_up(): return paddle_up(left_pad)
    def paddle_left_down(): return paddle_down(left_pad)
    def paddle_right_up(): return paddle_up(right_pad)
    def paddle_right_down(): return paddle_down(right_pad)

    # Hint: You can check documentations: https://docs.python.org/3/library/turtle.html#turtle.onkeypress

    screen.listen()
    # TODO listen for key 'w' and call paddle_left_up
    # TODO listen for key 's' and call paddle_left_down
    # TODO listen for key 'Up' and call paddle_right_up
    # TODO listen for key 'Down' and call paddle_right_up
