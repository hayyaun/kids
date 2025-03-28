

# Check Rocket and Ball collision


def check_ball_hit_rocket(ball, left_pad, right_pad):

    ball_x = ball.xcor()
    ball_y = ball.ycor()

    right_rocket_y = right_pad.ycor()
    left_rocket_y = left_pad.ycor()

    # TODO check if ball hit left rocket
    # ( 360 < ball_x < 370 ) and ( right_rocket_y - 50 < ball_y < right_rocket_y + 50 )

    # TODO then -> change horizontal direction (ball.dx *= -1)
    # also move ball back to -360 (left) or 360 (right)
