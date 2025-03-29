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
    # اگه توپ هم از لحاظ افقی و هم عمودی نزدیک راکت بود: توپ برمیگرده
    if ...:  # TODO
        # منظور از نزدیک بودن افقی یعنی
        # (left_rocket_x - 5 < ball_x < left_rocket_x + 5)
        # منظور از نزدیک بودن عمودی یعنی
        # (left_rocket_y - 50 < ball_y < left_rocket_y + 50)

        # منظور از برگشتن توپ یعنی جهت حرکت افقیش برعکس میشه
        ball.dx *= -1
        # همچنین باید به محل قبلی برای شروع مجدد برگرده یعنی:
        ball.setx(left_rocket_x)

    # 2. بررسی برخورد توپ با راکت سمت راست
    # مراحل قبل این بار برای راکت سمت راست تکرار میشه...
    # TODO
