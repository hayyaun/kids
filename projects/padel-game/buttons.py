import turtle


def show_pause_btn():
    # فقط یه دکنه استوپ سمت راست تابلو امتیازات اضافه شه
    # TODO
    return


def show_reset_btn(reset_btn: turtle.Turtle | None, show: bool):
    # 1. اگر حالت جدید مثل قبلی بود کاری نکن! و همون قبلی رو برگردون
    if reset_btn.show == show:
        return reset_btn
    # اگه حالت جدید با قبل فرف داشت پس جدید رو نشون بده
    # 2. ذخیره حالت جدید در دکمه
    reset_btn.show = show
    # 3. clear previous reset_btn
    # دکمه ریست قبلی « در صورت وجود » پاک بشه
    if reset_btn != None:
        reset_btn.clear()
    # 4. اگه حالت نمایش خاموش بود دکمه جدیدی رسم نکن
    if show == False:
        return reset_btn
    # 5. create new_reset_btn
    # دکمه جدید رسم بشه
    # TODO
    # 6. return new_reset_btn
    # دکمه جدید برگردونده شه
    return  # TODO
