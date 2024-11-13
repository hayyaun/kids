import time
import turtle

from ball import create_ball
from borders import check_hit_borders
from collision import check_ball_paddle_collision
from keyboard import add_keyboard_bindings
from move_paddle import (paddle_left_down, paddle_left_up, paddle_right_down,
                         paddle_right_up)
from paddle import create_paddle
from score import create_score_board, show_scores
from screen import create_screen

if __name__ == '__main__':

    # Create screen
    screen = create_screen(1000, 600)

    # Create Left paddle
    left_pad = create_paddle(-400)

    # Create Right paddle
    right_pad = create_paddle(400)

    # Create a Ball
    ball = create_ball()
    ball.dx = 5
    ball.dy = -5

    # Initialize the scores
    left_player = 0
    right_player = 0

    # Displays the score board
    score_board = create_score_board()
    show_scores(score_board, left_player, right_player)

    # Keyboard bindings
    add_keyboard_bindings(screen,
                          lambda: paddle_left_up(left_pad),
                          lambda: paddle_left_down(left_pad),
                          lambda: paddle_right_up(right_pad),
                          lambda: paddle_right_down(right_pad))

    # Main game loop
    while True:
        screen.update()
        time.sleep(0.01)  # Add delay to make game smoother

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Checking hit borders
        check_hit_borders(ball, 480, 280,
                          update_scores=lambda: show_scores(score_board, left_player, right_player))

        # Paddle ball collision
        check_ball_paddle_collision(ball, left_pad, right_pad)
