
def add_keyboard_bindings(screen, paddle_left_up, paddle_left_down, paddle_right_up, paddle_right_down):
    screen.listen()
    screen.onkeypress(paddle_left_up, "w")  # Changed to 'w'
    screen.onkeypress(paddle_left_down, "s")  # Changed to 's'
    screen.onkeypress(paddle_right_up, "Up")
    screen.onkeypress(paddle_right_down, "Down")
