import turtle


def create_score_board():
    score_board = turtle.Turtle()
    score_board.speed(0)  # TODO scoreboard has 0 speed
    score_board.color("blue")  # TODO add color to scoreboard
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, 260)  # TODO move scoreboard to (0, 260) coordinate
    return score_board


def show_scores(score_board, left_player, right_player):
    score_board.clear()
    # TODO write scores
    scores = f"Left_player : {left_player}    Right_player: {right_player}"
    score_board.write(scores, align="center", font=("Courier", 24, "normal"))
