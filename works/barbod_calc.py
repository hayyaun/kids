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
    answer = eval(equation)
    l_answer.config(text=answer)


# window
master = Tk()
master.resizable(False, False)
master.title('Calculator')
master.geometry('270x350')
master.configure(bg='gray')

# labels
l_equation = Label(master, font="20", bg="white",
                   height=2, width=24, anchor="e", padx=2)
l_equation.place(x=10, y=10)
l_equal = Label(master, text='=', font='20', bg='gray')
l_equal.place(x=10, y=70)
l_answer = Label(master, font='20', width=12)
l_answer.place(x=130, y=70)

# numbers
n1 = Button(master, text='1', font='16', width=4,
            height=2, command=append_equation('1'))
n1.place(x=10, y=110)
n2 = Button(master, text='2', font='16', width=4,
            height=2, command=append_equation('2'))
n2.place(x=70, y=110)
n3 = Button(master, text='3', font='16', width=4,
            height=2, command=append_equation('3'))
n3.place(x=130, y=110)
n4 = Button(master, text='4', font='16', width=4,
            height=2, command=append_equation('4'))
n4.place(x=10, y=170)
n5 = Button(master, text='5', font='16', width=4,
            height=2, command=append_equation('5'))
n5.place(x=70, y=170)
n6 = Button(master, text='6', font='16', width=4,
            height=2, command=append_equation('6'))
n6.place(x=130, y=170)
n7 = Button(master, text='7', font='16', width=4,
            height=2, command=append_equation('7'))
n7.place(x=10, y=230)
n8 = Button(master, text='8', font='16', width=4,
            height=2, command=append_equation('8'))
n8.place(x=70, y=230)
n9 = Button(master, text='9', font='16', width=4,
            height=2, command=append_equation('9'))
n9.place(x=130, y=230)
n10 = Button(master, text='AC', font='16', bg='red', width=4,
             height=2, command=delete)
n10.place(x=10, y=290)
n0 = Button(master, text='0', font='16', width=4,
            height=2, command=append_equation('0'))
n0.place(x=70, y=290)

# signs
eq = Button(master, text='=', font='16', bg='purple',
            width=4, height=2, command=calculate)
eq.place(x=130, y=290)
plus = Button(master, text='+', font='16', bg='purple',
              width=4, height=2, command=append_equation('+'))
plus.place(x=190, y=290)
minus = Button(master, text='-', font='16', bg='purple',
               width=4, height=2, command=append_equation('-'))
minus.place(x=190, y=230)
prod = Button(master, text='*', bg='purple', font='16',
              width=4, height=2, command=append_equation('*'))
prod.place(x=190, y=170)
div = Button(master, text='÷', font='16', bg='purple',
             width=4, height=2, command=append_equation('/'))
div.place(x=190, y=110)

# run
master.mainloop()
