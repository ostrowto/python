# input_fields.py

from tkinter import *

root = Tk()

my_Entry_1 = Entry(root, width = 50, borderwidth = 5, bg = 'grey', fg = 'white')
my_Entry_1.pack()
#my_Entry_1.get()
#my_Entry_1.insert(0, ' Please enter Your name here: ')

def my_Click():
    my_Click_to_Print = 'Your Name is: ' + my_Entry_1.get()
    my_Label = Label(root, text = my_Click_to_Print, fg = 'darkblue')
    my_Label.pack()

my_Button = Button(root, text = 'Enter Your Name', command = my_Click, fg = 'blue', bg = 'red')

my_Button.pack()

root.mainloop()
