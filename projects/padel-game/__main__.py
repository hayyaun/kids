import time

from colors import *
from borders import check_ball_hit_borders
from rockets import check_ball_hit_rocket
from keys import add_keyboard_bindings
from scene import create_ball, create_rocket, create_screen
from score import create_score_board, show_scores

if __name__ == '__main__':

    # Create screen - ساخت صفحه بازی
    screen = create_screen(1000, 600, bg_color)
    # Create Left rocket - ساخت راکت سمت چپ
    left_pad = create_rocket(-490, player_left_color)
    # Create Right rocket - ساخت راکت سمت راست
    right_pad = create_rocket(485, player_right_color)

    # Create a Ball - ساخت توپ
    ball = create_ball(ball_color)
    ball.dx = 5  # سرعت افقی توپ
    ball.dy = -5  # سرعت عمودی توپ

    # Players scores - امتیازات بازیکن ها
    scores = {
        "left": 2,  # امتیاز بازیکن چپ
        "right": 3  # امیتاز بازیکن راست
    }

    # Displays the score board - ساخت تابلو امتیازات
    score_board = create_score_board(scores)
    show_scores(score_board, scores)

    # تابعی که در صورت تغییرات امتیازات باید صدا شود
    def update_scores(): return show_scores(score_board, scores)

    # Keyboard bindings - for rocket movement - حرکت راکت با کیبورد
    add_keyboard_bindings(screen, left_pad, right_pad)

    # Main game loop - حلقه اصلی بازی
    while True:
        screen.update()  # اعمال تغییرات
        # Add delay to make game smoother - وقفه یک صدم ثانیه ای قبل از اجرای دور حلقه
        time.sleep(0.01)

        # Update ball x, y - تغییر مختصات افقی و عمودی توپ
        # به اندازه ی سرعتی که داری برو جلو/عقب
        ball.setx(ball.xcor() + ball.dx)
        # به اندازه سرعتی که داری برو بالا/پایین
        ball.sety(ball.ycor() + ball.dy)

        # Checking ball hit borders - بررسی برخورد توپ با کناره های زمین (دیواری / امتیاز)
        check_ball_hit_borders(ball, 480, 280, scores, update_scores)

        # Rocket ball collision - بررسی برخورد توپ با راکت ها
        check_ball_hit_rocket(ball, left_pad, right_pad)
