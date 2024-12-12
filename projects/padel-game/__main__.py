import time

from borders import check_hit_borders
from collision import check_ball_paddle_collision
from keyboard import add_keyboard_bindings
from scene import create_ball, create_paddle, create_screen
from score import create_score_board, show_scores

if __name__ == '__main__':

    # Create screen
    # FIXME screen = create_screen(1000, 600)
    # Create Left paddle
    # FIXME left_pad = create_paddle(-400)
    # Create Right paddle
    # FIXME right_pad = create_paddle(400)
    # Create a Ball
    # FIXME ball = create_ball()
    # FIXME ball.dx = 5
    # FIXME ball.dy = -5

    # Displays the score board
    # FIXME score_board = create_score_board()
    # FIXME score_board.left_player = 0
    # FIXME score_board.right_player = 0
    # FIXME show_scores(score_board)

    # Keyboard bindings - for paddle movement
    # FIXME add_keyboard_bindings(screen, left_pad, right_pad)

    # Main game loop
    while True:
        # FIXME screen.update()
        time.sleep(0.01)  # Add delay to make game smoother

        # Update ball x, y
        # FIXME ball.setx(ball.xcor() + ball.dx)
        # FIXME ball.sety(ball.ycor() + ball.dy)

        # Checking hit borders
        # FIXME def update_scores(): return show_scores(score_board)
        # FIXME check_hit_borders(ball, 480, 280, score_board, update_scores)

        # Paddle ball collision
        # FIXME check_ball_paddle_collision(ball, left_pad, right_pad)
