from tkinter import *


equation = ""


def append_equation(s):
    def append_s():
        global equation
        equation += s
        l_equation.config(text=equation)
    return append_s


def delete():
    global equation
    equation = ""
    l_equation.config(text=equation)
    l_answer.config(text=equation)


def calculate():
    answer: float = eval(equation)
    answer = round(answer, 2)
    l_answer.config(text=answer)


# window
master = Tk()
master.resizable(False, False)
master.title('کله کولاتور')
master.geometry('255x350')
master.configure(bg='gray')

# labels
l_equation = Label(master, font="20", bg="white",
                   height=2, width=23, anchor="e", padx=3)
l_equation.place(x=10, y=10)
l_equal = Label(master, text='=', font='20', bg='gray')
l_equal.place(x=10, y=70)
l_answer = Label(master, font='20', width=11)
l_answer.place(x=130, y=70)


# buttons
ac = Button(master, text='AC', font='16', bg='red', width=3,
            height=2, command=delete)
ac.place(x=10, y=290)
eq = Button(master, text='=', font='16', bg='purple',
            width=3, height=2, command=calculate)
eq.place(x=130, y=290)

# keys
keys = [
    ('1', 10, 110, None), ('2', 70, 110, None),
    ('3', 130, 110, None), ('4', 10, 170, None),
    ('5', 70, 170, None), ('6', 130, 170, None),
    ('7', 10, 230, None), ('8', 70, 230, None),
    ('9', 130, 230, None), ('0', 70, 290, None),
    ('+', 190, 290, 'purple'), ('-', 190, 230, 'purple'),
    ('*', 190, 170, 'purple'), ('/', 190, 110, 'purple'),
]

for key in keys:
    btn = Button(master, text=key[0], font='16', width=3,
                 height=2, command=append_equation(key[0]), bg=key[3])
    btn.place(x=key[1], y=key[2])


# run
master.mainloop()

# salam barbod!
