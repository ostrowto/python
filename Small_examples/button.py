# buton.py

from tkinter import *

root = Tk()

def my_Click():
    my_Label = Label(root, text = 'This button was clicked!', fg = 'darkblue')
    my_Label.pack()

my_Button = Button(root, text = 'Click me!', command = my_Click, fg = 'blue', bg = 'red')

my_Button.pack()

root.mainloop()
