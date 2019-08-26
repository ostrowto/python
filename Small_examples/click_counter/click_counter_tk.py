from tkinter import *
from tkinter import messagebox

def click_counter(x):
    return 'You`ve clicked:\n' + str(x)

counter_of_click = 0

def clickable():
    global counter_of_click, text_to_click
    counter_of_click += 1
    text_to_click.set(click_counter(counter_of_click))

def close_window():
    if(messagebox.askyesno('Attention!', 'Really close ... ?')):
        object_to_click.destroy()


counter_of_click = 0
object_to_click = Tk()
object_to_click.title('Click counter!')


my_Button = Button(object_to_click, text = 'Click me!', bg = 'red', fg = 'yellow', command = clickable)
my_Button.pack(pady=20)

object_to_click.minsize(width=250, height=200)
object_to_click.maxsize(width=350, height=250)

object_to_click.geometry('200x100')
object_to_click.protocol('WM_DELETE_WINDOW', close_window)

text_to_click = StringVar()
my_Label = Label(object_to_click, textvariable = text_to_click, height = 4)
text_to_click.set(click_counter(counter_of_click))
my_Label.pack()

object_to_click.mainloop()

