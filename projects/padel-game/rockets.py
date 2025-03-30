import turtle


def check_ball_hit_rocket(ball: turtle.Turtle, left_rocket: turtle.Turtle, right_rocket: turtle.Turtle):
    ''' متغیر های مورد نیاز برای محاسبات '''

    ball_x = ball.xcor()  # موقعیت افقی توپ
    ball_y = ball.ycor()  # موقعیت عمودی توپ

    left_rocket_x = left_rocket.xcor()  # موقعیت افقی راکت چپ
    left_rocket_y = left_rocket.ycor()  # موقعیت عمودی راکت چپ
    right_rocket_x = right_rocket.xcor()  # موقعیت افقی راکت راست
    right_rocket_y = right_rocket.ycor()  # موقعیت عمودی راکت راست

    ''' محاسبات اصلی '''

    # 1. بررسی برخورد توپ با راکت سمت چپ

    hit_threshold_x = 10  # فاصله افقی مجاز برای برخورد
    hit_threshold_y = 50  # فاصله عمودی راکت که توپ باید داخلش باشه

    # 1. بررسی برخورد توپ با راکت سمت چپ
    # اگه توپ هم از لحاظ افقی و هم عمودی نزدیک راکت بود: توپ برمیگرده
    if abs(ball_x - left_rocket_x) < hit_threshold_x and (left_rocket_y - hit_threshold_y < ball_y < left_rocket_y + hit_threshold_y):
        ball.dx *= -1  # تغییر جهت حرکت افقی توپ
        # جابجایی توپ به بیرون از راکت برای جلوگیری از عبور
        ball.setx(left_rocket_x + hit_threshold_x)

    # 2. بررسی برخورد توپ با راکت سمت راست
    if abs(ball_x - right_rocket_x) < hit_threshold_x and (right_rocket_y - hit_threshold_y < ball_y < right_rocket_y + hit_threshold_y):
        ball.dx *= -1
        ball.setx(right_rocket_x - hit_threshold_x)
