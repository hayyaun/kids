
# Functions to move paddle


def paddle_up(pad):
    y = pad.ycor()
    if y < 250:  # check if paddle y is less than 250
        y += 20  # TODO then move pad up +20 and set y
        pad.sety(y)


def paddle_down(pad):
    y = pad.ycor()
    if y > -240:  # check if paddle y is bigger than -240
        y -= 20  # TODO then move pad down -20 and set y
        pad.sety(y)


# Create Keyboard Bindings to move paddles


def add_keyboard_bindings(screen, left_pad, right_pad):

    def paddle_left_up(): return paddle_up(left_pad)
    def paddle_left_down(): return paddle_down(left_pad)
    def paddle_right_up(): return paddle_up(right_pad)
    def paddle_right_down(): return paddle_down(right_pad)

    screen.listen()
    # listen for key 'w' and call paddle_left_up
    screen.onkeypress(paddle_left_up, "w")  # TODO
    # listen for key 's' and call paddle_left_down
    screen.onkeypress(paddle_left_down, "s")  # TODO
    # listen for key 'Up' and call paddle_right_up
    screen.onkeypress(paddle_right_up, "Up")  # TODO
    # listen for key 'Down' and call paddle_right_up
    screen.onkeypress(paddle_right_down, "Down")  # TODO
