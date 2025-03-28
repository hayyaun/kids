import turtle

# Check if Ball hits border

# Hint: You can read documentations: https://docs.python.org/3/library/turtle.html#turtle.goto


def reset_ball_position(ball: turtle.Turtle):
    # برگرداندن توپ به حالت اول برای شروع مجدد
    ball.goto(0, 0)  # برو وسط صفحه
    ball.dy *= -1


def check_ball_hit_borders(ball: turtle.Turtle, lim_x: int, lim_y: int, scores: dict, update_scores: function):

    ball_x = ball.xcor()  # موقعیت افقی توپ
    ball_y = ball.ycor()  # موقعیت عمودی توپ

    border_left_x = -lim_x  # موقعیت افقی دیوار چپ
    border_right_x = lim_x  # موقعیت افقی دیوار راست

    border_top_y = lim_y  # موقعیت عمودی دیوار بالا
    border_bottom_y = -lim_y  # موقعیت عمودی دیوار پایین

    """ دیوار های عمودی (بالا/پایین) """

    # 1. اگه توپ به دیوار بالا برخورد کنه برمیگرده
    # منظور از برخورد با دیوار بالا یعنی: ball_y > border_top_y
    # منظور از برگشتن توپ یعنی جهت حرکت عمودیش برعکس میشه
    ball.dy *= -1
    # همچنین باید به محل قبلی برای شروع مجدد برگرده
    ball.sety(border_top_y)

    # 2. اگه توپ به دیوار پایین برخورد کنه برمیگرده
    # منظور از برخورد با دیوار بالا یعنی: ball_y < border_bottom_y
    # منظور از برگشتن توپ یعنی جهت حرکت عمودیش برعکس میشه
    # TODO
    # همچنین باید به محل قبلی برای شروع مجدد برگرده
    # TODO

    """ دیوار های افقی (چپ/راست) """

    # 3. اگه توپ به دیوار سمت چپ برخورد کرد -> امتیاز بازیکن راست
    # منظور از برخورد با دیوار چپ یعنی: ball_x < border_left_x
    # Reset Ball Position - شروع مجدد توپ
    reset_ball_position()
    # Right player Scored - بازیکن راست امتیاز گرفت
    scores.right += 1
    # update scores - اعلام تغییرات به تابلو امتیازات
    update_scores()

    # 4. اگه توپ به دیوار سمت راست برخورد کرد -> امتیاز بازیکن چپ
    # منظور از برخورد با دیوار راست یعنی: ball_x > border_right_x
    # Reset Ball Position - شروع مجدد توپ
    # TODO
    # Left player Scored - بازیکن چپ امتیاز گرفت
    # TODO
    # update scores - اعلام تغییرات به تابلو امتیازات
    # TODO
