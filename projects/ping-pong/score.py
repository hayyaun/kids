import turtle


def create_score_board():
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.color("blue")
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, 260)
    return score_board


def show_scores(score_board, left_player, right_player):
    score_board.clear()
    score_board.write(f"Left_player : {left_player}    Right_player: {right_player}",
                      align="center", font=("Courier", 24, "normal"))
