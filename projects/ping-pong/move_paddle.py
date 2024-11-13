# Functions to move paddles

def paddle_left_up(left_pad):
    y = left_pad.ycor()
    if y < 250:  # Limit paddle movement
        y += 20
        left_pad.sety(y)


def paddle_left_down(left_pad):
    y = left_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        left_pad.sety(y)


def paddle_right_up(right_pad):
    y = right_pad.ycor()
    if y < 250:  # Limit paddle movement
        y += 20
        right_pad.sety(y)


def paddle_right_down(right_pad):
    y = right_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        right_pad.sety(y)
