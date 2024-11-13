def check_hit_borders(ball, dx, dy, left_player, right_player, update_scores):
    ball_x = ball.xcor()
    ball_y = ball.ycor()

    if ball_y > dy:
        ball.sety(dy)
        ball.dy *= -1

    elif ball_y < -dy:
        ball.sety(-dy)
        ball.dy *= -1

    elif ball_x > dx:
        # Reset ball position
        ball.goto(0, 0)
        ball.dy *= -1
        # Left player Scored
        left_player += 1
        update_scores()

    elif ball_x < -dx:
        # Reset ball position
        ball.goto(0, 0)
        ball.dy *= -1
        # Right player Scored
        right_player += 1
        update_scores()
