
def add_keyboard_bindings(screen, paddle_left_up, paddle_left_down, paddle_right_up, paddle_right_down):
    screen.listen()
    # listen for key 'w' and call paddle_left_up
    screen.onkeypress(paddle_left_up, "w")  # TODO
    # listen for key 's' and call paddle_left_down
    screen.onkeypress(paddle_left_down, "s")  # TODO
    # listen for key 'Up' and call paddle_right_up
    screen.onkeypress(paddle_right_up, "Up")  # TODO
    # listen for key 'Down' and call paddle_right_up
    screen.onkeypress(paddle_right_down, "Down")  # TODO
