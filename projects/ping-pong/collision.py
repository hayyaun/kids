def check_ball_paddle_collision(ball, left_pad, right_pad):
    if (ball.xcor() > 360 and ball.xcor() < 370) and \
            (ball.ycor() < right_pad.ycor() + 50 and ball.ycor() > right_pad.ycor() - 50):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and \
            (ball.ycor() < left_pad.ycor() + 50 and ball.ycor() > left_pad.ycor() - 50):
        ball.setx(-360)
        ball.dx *= -1
