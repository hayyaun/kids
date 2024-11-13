def check_hit_borders(ball, dx, dy, update_scores):
    if ball.ycor() > dy:
        ball.sety(dy)
        ball.dy *= -1

    if ball.ycor() < -dy:
        ball.sety(-dy)
        ball.dy *= -1

    if ball.xcor() > dx:
        # Reset ball position
        ball.goto(0, 0)
        ball.dy *= -1
        # Left player Scored
        left_player += 1
        update_scores()

    if ball.xcor() < -dx:
        # Reset ball position
        ball.goto(0, 0)
        ball.dy *= -1
        # Right player Scored
        right_player += 1
        update_scores()
