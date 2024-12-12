import turtle

# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.color
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.goto
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.speed
# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.write


def create_score_board():
    # Create score board
    score_board = turtle.Turtle()
    # TODO scoreboard has 0 speed
    # TODO add color to scoreboard
    score_board.penup()
    score_board.hideturtle()
    # TODO move scoreboard to (0, 260) coordinate
    return score_board


def show_scores(score_board):
    # Show scores of each player
    score_board.clear()
    left_score = score_board.left_player
    right_score = score_board.right_player
    scores = f"Left: {left_score}       Right: {right_score}"
    # TODO write scores, aligned at center, with a good font
