

# Check Rocket and Ball collision


def check_ball_rocket_collision(ball, left_pad, right_pad):

    ball_x = ball.xcor()
    ball_y = ball.ycor()

    right_pad_y = right_pad.ycor()
    left_pad_y = left_pad.ycor()

    if (ball_x > 360 and ball_x < 370) and \
            (ball_y < right_pad_y + 50 and ball_y > right_pad_y - 50):
        ball.setx(360)
        ball.dx *= -1

    if (ball_x < -360 and ball_x > -370) and \
            (ball_y < left_pad_y + 50 and ball_y > left_pad_y - 50):
        ball.setx(-360)
        ball.dx *= -1
