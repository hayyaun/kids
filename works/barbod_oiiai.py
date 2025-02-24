from tkinter import *
import random
a = 1
is_first = True
while 1:
    x = random.randint(0, 100)
    c = random.randint(0, x)
    d = random.randint(0, 50)
    e = random.randint(0, 20)
    g = random.randint(0, 70)
    y = random.randint(0, 100)
    komak = [x, e, d, c, g, y]

    def bababoy():
        b = e1.get()
        if b != x:
            l2.config(text='hads shoma eshtebah bood')
            l3.config(text='aya komak mikhahid?')

            def mamamia():
                h = e2.get()
                if h == 'yes':
                    l4.config(text='yeki az adade zir gavab hast:')
                    random.shuffle(komak)
                    l5.config(text=komak)
                    l6.config(text='hads khod ra vared konid:')

                    def nmdnm():
                        w = e3.get()
                        if w == x:
                            l7.config(text='afarin hadset dorost bood')
                        if w != x:
                            l8.config(text='hads shoma eshtebah bood')

                    b3 = Button(win, width=10, font='20',
                                text='go', command=nmdnm)
                    b3.place(x=300, y=415)
                    e3 = Entry(win, width=10, font='50')
                    e3.place(x=180, y=420)
            e2 = Entry(win, width=10, font='50')
            e2.place(x=180, y=210)
            b2 = Button(win, width=10, font='20', text='go', command=mamamia)
            b2.place(x=300, y=205)

        if b == x:
            l2.config(text="afarin hadset dorost bood")
    win = Tk()
    win.geometry('600x600')
    win.configure(bg='gray')
    win.title('barbod game')
    l1 = Label(win, text='yek adad beyne 0 ta 100 hads bezanin:',
               font='50', width=40, bg='gray')
    l1.place(x=120, y=30)
    l2 = Label(win, font='80', width=40, bg='gray', fg='red')
    l2.place(x=100, y=120)
    l3 = Label(win, font='60', width=40, bg='gray')
    l3.place(x=100, y=160)
    l4 = Label(win, font='20', width=40, bg='gray')
    l4.place(x=100, y=270)
    l5 = Label(win, font='20', width=40, bg='gray')
    l5.place(x=100, y=310)
    l6 = Label(win, font='100', width=40, bg='gray')
    l6.place(x=100, y=350)
    l7 = Label(win, font='100', width=40, bg='gray', fg='green')
    l7.place(x=100, y=460)
    l8 = Label(win, font='100', width=40, bg='gray', fg='red')
    l8.place(x=100, y=460)
    l9 = Label(win, font='20', width=40, bg='gray')
    l9.place(x=100, y=480)
    e1 = Entry(win, width=10, font='22')
    e1.place(x=180, y=70)
    b1 = Button(win, width=10, font='20', text='go', command=bababoy)
    b1.place(x=300, y=65)
    win.mainloop()
