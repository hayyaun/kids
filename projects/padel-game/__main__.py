import time

from colors import *
from borders import check_hit_borders
from collision import check_ball_rocket_collision
from keys import add_keyboard_bindings
from scene import create_ball, create_rocket, create_screen
from score import create_score_board, show_scores

if __name__ == '__main__':

    # Create screen
    screen = create_screen(1000, 600, bg_color)
    # Create Left rocket
    left_pad = create_rocket(-490, player_left_color)
    # Create Right rocket
    right_pad = create_rocket(485, player_right_color)
    # Create a Ball
    ball = create_ball(ball_color)
    ball.dx = 5
    ball.dy = -5

    # Displays the score board
    # FIXME score_board = create_score_board()
    # FIXME score_board.left_player = 0
    # FIXME score_board.right_player = 0
    # FIXME show_scores(score_board)

    # Keyboard bindings - for rocket movement
    # FIXME add_keyboard_bindings(screen, left_pad, right_pad)

    # Main game loop
    while True:
        screen.update()
        time.sleep(0.01)  # Add delay to make game smoother

        # Update ball x, y
        # FIXME ball.setx(ball.xcor() + ball.dx)
        # FIXME ball.sety(ball.ycor() + ball.dy)

        # Checking ball hit borders
        # FIXME def update_scores(): return show_scores(score_board)
        # FIXME check_ball_hit_borders(ball, 480, 280, score_board, update_scores)

        # Rocket ball collision
        # FIXME check_ball_rocket_collision(ball, left_pad, right_pad)
