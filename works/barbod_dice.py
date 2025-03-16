from tkinter import *
import random


def main():

    def try_again():
        x.destroy()
        main()

    def append_label(s):

        def append():
            y = ""
            y += s
            l1.config(text=y)
            b1.config(state='disabled')
            b2.config(state='disabled')
            b3.config(state='disabled')
            b4.config(state='disabled')
            b5.config(state='disabled')
            b6.config(state='disabled')
            r = ['2', '4']
            r2 = random.choice(r)
            if r2 == "1":
                lr1 = Label(x, text='  0  ', width=7, height=3)
                lr1.place(x=125, y=170)
            if r2 == "2":
                lr2 = Label(x, text='      0', width=7, height=1)
                lr2.place(x=125, y=160)
                lr23 = Label(x, text='       ', width=7)
                lr23.place(x=125, y=180)
                lr22 = Label(x, text='0      ', width=7, height=1)
                lr22.place(x=125, y=200)
            if r2 == "3":
                lr31 = Label(x, text='           0', width=7)
                lr31.place(x=125, y=170)
                lr32 = Label(x, text='      0     ', width=7)
                lr32.place(x=125, y=190)
                lr33 = Label(x, text='0           ', width=7)
                lr33.place(x=125, y=210)
            if r2 == "4":
                lr41 = Label(x, text='0     0', width=7)
                lr41.place(x=125, y=160)
                lr43 = Label(x, text='       ', width=7)
                lr43.place(x=125, y=180)
                lr42 = Label(x, text='0     0', width=7)
                lr42.place(x=125, y=200)
            if r2 == "5":
                lr51 = Label(x, text='0        0', width=7)
                lr51.place(x=125, y=170)
                lr52 = Label(x, text='     0    ', width=7)
                lr52.place(x=125, y=190)
                lr53 = Label(x, text='0        0', width=7)
                lr53.place(x=125, y=210)
            if r2 == "6":
                lr61 = Label(x, text=' 0 0 0 ', width=6)
                lr61.place(x=125, y=170)
                lr63 = Label(x, text='       ', width=6)
                lr63.place(x=125, y=190)
                lr62 = Label(x, text=' 0 0 0 ', width=6)
                lr62.place(x=125, y=200)

            if s == r2:
                sl1 = Label(x, text='afarin hadset dorost bood',
                            fg='green', bg='gray', font=17)
                sl1.place(x=50, y=300)
            if s != r2:
                sl2 = Label(x, text='hadset eshtebah bood',
                            fg='red', bg='gray', font=17)
                sl2.place(x=70, y=300)

        return append
    # tkinter
    x = Tk()
    x.geometry('300x350')
    x.configure(bg='gray')
    # Labels
    l1 = Label(x, text='', )
    l1.place(x=150, y=25)
    l2 = Label(x, text='hads bezanid tas che adadi ro neshun mide', bg="gray")
    l2.place(x=20, y=5)
    # Buttons
    b1 = Button(x, text='1', width=1, command=append_label("1"))
    b1.place(x=70, y=55)
    b2 = Button(x, text='2', command=append_label("2"))
    b2.place(x=135, y=55)
    b3 = Button(x, text='3', command=append_label("3"))
    b3.place(x=200, y=55)
    b4 = Button(x, text='4', command=append_label("4"))
    b4.place(x=70, y=95)
    b5 = Button(x, text='5', command=append_label("5"))
    b5.place(x=135, y=95)
    b6 = Button(x, text='6', command=append_label("6"))
    b6.place(x=200, y=95)
    bt = Button(x, text='try again', command=try_again)
    bt.place(x=110, y=250)
    # tas

    x.mainloop()


main()
