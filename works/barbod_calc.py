from tkinter import *


equation = ""


def caculator(s: str):
    def calculate():
        global equation
        equation += s
        l_equation.config(text=equation)
    return calculate


def evaluate():
    answer = eval(equation)
    l_answer.config(text=answer)


# window
master = Tk()
master.resizable(False, False)
master.title('Calculator')
master.geometry('450x400')
master.configure(bg='gray')

# labels
l_equation = Label(master, font="20", bg="white", width=25, anchor="e")
l_equation.place(x=120, y=30)
l_equal = Label(master, text='=', font='20', bg='gray',)
l_equal.place(x=120, y=70)
l_answer = Label(master, font='20', width=7)
l_answer.place(x=300, y=70)

# numbers
n1 = Button(master, text='1', font='16', width=4,
            height=2, command=caculator('1'))
n1.place(x=120, y=110)
n2 = Button(master, text='2', font='16', width=4, height=2)
n2.place(x=180, y=110)
n3 = Button(master, text='3', font='16', width=4, height=2)
n3.place(x=240, y=110)
n4 = Button(master, text='4', font='16', width=4, height=2)
n4.place(x=120, y=170)
n5 = Button(master, text='5', font='16', width=4, height=2)
n5.place(x=180, y=170)
n6 = Button(master, text='6', font='16', width=4, height=2)
n6.place(x=240, y=170)
n7 = Button(master, text='7', font='16', width=4, height=2)
n7.place(x=120, y=230)
n8 = Button(master, text='8', font='16', width=4, height=2)
n8.place(x=180, y=230)
n9 = Button(master, text='9', font='16', width=4, height=2)
n9.place(x=240, y=230)
n10 = Button(master, text='AC', font='16', bg='red', width=4, height=2)
n10.place(x=120, y=290)
n0 = Button(master, text='0', font='16', width=4, height=2)
n0.place(x=180, y=290)

# signs
eq = Button(master, text='=', font='16', bg='purple',
            width=4, height=2, command=evaluate)
eq.place(x=240, y=290)
plus = Button(master, text='+', font='16', bg='purple', width=4, height=2)
plus.place(x=300, y=290)
minus = Button(master, text='-', font='16', bg='purple', width=4, height=2)
minus.place(x=300, y=230)
prod = Button(master, text='*', bg='purple', font='16', width=4, height=2)
prod.place(x=300, y=170)
div = Button(master, text='÷', font='16', bg='purple', width=4, height=2)
div.place(x=300, y=110)

# run
master.mainloop()
