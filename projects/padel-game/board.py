import turtle
from colors import *


def create_score_board(scores):
    # Create score board - ساخت تابلوی امتیازات
    score_board = turtle.Turtle()
    score_board.speed(100)

    # Create main box - ساخت جعبه ی اصلی
    # Left triangle - مثلث چپ
    create_triangle(score_board, -153)
    # Right triangle - مثلث راست
    create_triangle(score_board, 99)
    # main box - مستطیل تابلوی امتیازات
    draw_colored_box(score_board, black, -137, 263, 250, 27)
    # Left color box - مستطیل رنگی چپ
    draw_colored_box(score_board, "black", -54, 263, 2, 27)
    # Right color box - کستطیل رنگی راست
    draw_colored_box(score_board, "black", 18, 263, 2, 27)

    # Write texts - نوشتن متن ها
    writeTexts(score_board)

    # Left player lights - چراغ های بازیکن سمت چپ
    for i in range(5):
        light_color = white
        if scores["left"] > i:
            light_color = player_left_color
        draw_circle(score_board, light_color, -105 + 10*i)

    # Right player lights - چراغ های بازیکن سمت راست
    for i in range(5):
        light_color = white
        if scores["right"] > i:
            light_color = player_right_color
        draw_circle(score_board, light_color, 75 - 10*i)

    turtle.hideturtle()
    return score_board


def show_scores(score_board, scores):
    # Clear & Show scores of each player again - پاک کردن و نمایش مجدد امتیازات هر بازیکن
    score_board.clear()
    create_score_board(scores)


# NIKAN - نیکان

def create_triangle(t: turtle.Turtle, x):
    # ساخت دو مثلث کناری

    t.penup()
    t.goto(x, 290)
    t.pendown()
    t.color(black)
    t.begin_fill()

    # draw triangle - کشیدن مثلث
    for _ in range(3):
        t.forward(30)
        t.left(-120)

    t.end_fill()
    t.hideturtle()


def draw_colored_box(t: turtle.Turtle, color, x0, y0, width, height):
    # ساخت مستطیل های تابلوی امتیازات

    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.color(color)
    t.begin_fill()

    # draw rectangle - کشیدن مستطیل
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()
    t.hideturtle()


def writeTexts(t: turtle.Turtle):
    # نوشتن متن های درون تابلوی امتیازات

    # نوشتن کلمه ی «پدل» در وسط تابلوی امتیازات
    t.penup()
    t.goto(-45, 274)
    t.pendown()
    t.color(white)
    t.write("PADEL", font=("Lucida Handwriting", 7, "bold"))

    # نوشتن کلمه ی «بازی های» در وسط تابلوی امتیازات
    t.penup()
    t.goto(-20, 268)
    t.pendown()
    t.color(white)
    t.write("GAMES", font=("Algerian", 7, "bold"))

    # نوشتن کلمه ی «بازیکن شماره یک» در سمت چپ تابلوی امتیازات
    t.penup()
    t.goto(-112, 273)
    t.pendown()
    t.color(player_left_color)
    t.write("PLAYER 1", font=("Arial", 8, "bold"))
    t.hideturtle()

    # نوشتن کلمه ی «بازیکن شماره دو» در سمت راست تابلوی امتیازات
    t.penup()
    t.goto(34, 273)
    t.pendown()
    t.color(player_right_color)
    t.write("PLAYER 2", font=("Arial", 8, "bold"))
    t.hideturtle()


def draw_circle(t: turtle.Turtle, color, x):
    # ساخت دایره ها برای نمایش امتیازات بازیکنان
    t.penup()
    t.goto(x, 266)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.hideturtle()
