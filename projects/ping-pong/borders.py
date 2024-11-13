def check_hit_borders(ball, lim_x, lim_y, left_player, right_player, update_scores):

    ball_x = ball.xcor()
    ball_y = ball.ycor()

    # if ball y is bigger than limit y, reverse dy
    if ball_y > lim_y:
        ball.sety(lim_y)
        ball.dy *= -1  # TODO reverse dy

    # if ball y is less than limit y, reverse dy
    elif ball_y < -lim_y:
        ball.sety(-lim_y)
        ball.dy *= -1  # TODO reverse dy

    # if ball x is bigger than limit x, left player is scored!
    elif ball_x > lim_x:
        # Reset ball position
        ball.goto(0, 0)  # TODO go to (0,0) coordinate
        ball.dy *= -1  # TODO reverse dy
        # Left player Scored
        left_player += 1  # TODO increase left player score
        update_scores()

    # if ball x is less than limit x, right player is scored!
    elif ball_x < -lim_x:
        # Reset ball position
        ball.goto(0, 0)  # TODO go to (0,0) coordinate
        ball.dy *= -1  # TODO reverse dy
        # Right player Scored
        right_player += 1  # TODO increase right player score
        update_scores()
