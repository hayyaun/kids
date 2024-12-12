

# Check if Ball hits border

# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.goto


def check_hit_borders(ball, lim_x, lim_y, score_board, update_scores):

    ball_x = ball.xcor()
    ball_y = ball.ycor()

    # if ball y is bigger than limit y, reverse dy
        # UNCOMMENT ball.sety(lim_y)
        # TODO reverse dy

    # elif ball y is less than limit y, reverse dy
        # UNCOMMENT ball.sety(-lim_y)
        # TODO reverse dy

    # elif ball x is bigger than limit x, left player is scored!
        # Left player scored!
        # Reset ball position
        # TODO go to (0,0) coordinate
        # TODO reverse dy
        # Left player Scored
        # TODO increase left player score
        # TODO update scores

    # elif ball x is less than limit x, right player is scored!
        # Right player scored!
        # Reset ball position
        # TODO go to (0,0) coordinate
        # TODO reverse dy
        # Right player Scored
        # TODO increase right player score
        # TODO update scores
