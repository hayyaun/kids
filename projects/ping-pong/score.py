import turtle


# Create score board
def create_score_board():
    score_board = turtle.Turtle()
    score_board.speed(0)  # TODO scoreboard has 0 speed
    score_board.color("blue")  # TODO add color to scoreboard
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, 260)  # TODO move scoreboard to (0, 260) coordinate
    return score_board


# Show scores of each player
def show_scores(score_board,):
    score_board.clear()
    left_score = score_board.left_player
    right_score = score_board.right_player
    scores = f"Left: {left_score}       Right: {right_score}"
    # TODO write scores, aligned at center, with a good font
    score_board.write(scores, align="center", font=("Courier", 18, "normal"))
