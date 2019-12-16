# calc_on_tkinter.py

from tkinter import *


root = Tk()
root.title('Calculator on tkinter')

input_Values_Field = Entry(root, width=35, borderwidth=5)
input_Values_Field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def my_Button_Click(number):
    current = input_Values_Field.get()
    input_Values_Field.delete(0, END)
    input_Values_Field.insert(0, str(current) + str(number))


def my_Button_Clearing():
    input_Values_Field.delete(0, END)


def my_Button_Add():
    first_Number = input_Values_Field.get()
    global f_num
    global math_do
    math_do = 'my_addition'
    f_num = int(first_Number)
    input_Values_Field.delete(0, END)


def my_Button_Eq():
    second_Number = input_Values_Field.get()
    input_Values_Field.delete(0, END)

    if math_do == 'my_addition':
        input_Values_Field.insert(0, f_num + int(second_Number))

    if math_do == 'my_substraction':
        input_Values_Field.insert(0, f_num - int(second_Number))

    if math_do == 'my_multiplication':
        input_Values_Field.insert(0, f_num * int(second_Number))

    if math_do == 'my_division':
        input_Values_Field.insert(0, f_num / int(second_Number))


def my_Button_Sub():
    first_Number = input_Values_Field.get()
    global f_num
    global math_do
    math_do = 'my_substracion'
    f_num = int(first_Number)
    input_Values_Field.delete(0, END)


def my_Button_Mul():
    first_Number = input_Values_Field.get()
    global f_num
    global math_do
    math_do = 'my_multiplication'
    f_num = int(first_Number)
    input_Values_Field.delete(0, END)


def my_Button_Div():
    first_Number = input_Values_Field.get()
    global f_num
    global math_do
    math_do = 'my_division'
    f_num = int(first_Number)
    input_Values_Field.delete(0, END)


my_Button_1 = Button(root, text='1', padx=40, pady=20,
                     command=lambda: my_Button_Click(1))
my_Button_2 = Button(root, text='2', padx=40, pady=20,
                     command=lambda: my_Button_Click(2))
my_Button_3 = Button(root, text='3', padx=40, pady=20,
                     command=lambda: my_Button_Click(3))

my_Button_4 = Button(root, text='4', padx=40, pady=20,
                     command=lambda: my_Button_Click(4))
my_Button_5 = Button(root, text='5', padx=40, pady=20,
                     command=lambda: my_Button_Click(5))
my_Button_6 = Button(root, text='6', padx=40, pady=20,
                     command=lambda: my_Button_Click(6))

my_Button_7 = Button(root, text='7', padx=40, pady=20,
                     command=lambda: my_Button_Click(7))
my_Button_8 = Button(root, text='8', padx=40, pady=20,
                     command=lambda: my_Button_Click(8))
my_Button_9 = Button(root, text='9', padx=40, pady=20,
                     command=lambda: my_Button_Click(9))

my_Button_0 = Button(root, text='0', padx=40, pady=20,
                     command=lambda: my_Button_Click(0))

my_Button_Addition = Button(root, text='+', padx=39,
                            pady=20, command=my_Button_Add)
my_Button_Equal = Button(root, text='=', padx=86,
                         pady=20, command=my_Button_Eq)
my_Button_Clear = Button(root, text='Clear', padx=76,
                         pady=20, command=my_Button_Clearing)


my_Button_Substract = Button(
    root, text='-', padx=41, pady=20, command=my_Button_Sub)
my_Button_Multiply = Button(root, text='*', padx=40,
                            pady=20, command=my_Button_Mul)
my_Button_Divide = Button(root, text='/', padx=40,
                          pady=20, command=my_Button_Div)

my_Button_1.grid(row=3, column=0)
my_Button_2.grid(row=3, column=1)
my_Button_3.grid(row=3, column=2)

my_Button_4.grid(row=2, column=0)
my_Button_5.grid(row=2, column=1)
my_Button_6.grid(row=2, column=2)

my_Button_7.grid(row=1, column=0)
my_Button_8.grid(row=1, column=1)
my_Button_9.grid(row=1, column=2)

my_Button_0.grid(row=4, column=0)

my_Button_Addition.grid(row=5, column=0)
my_Button_Equal.grid(row=5, column=1, columnspan=2)
my_Button_Clear.grid(row=4, column=1, columnspan=2)

my_Button_Substract.grid(row=6, column=0)
my_Button_Multiply.grid(row=6, column=1)
my_Button_Divide.grid(row=6, column=2)

root.mainloop()
