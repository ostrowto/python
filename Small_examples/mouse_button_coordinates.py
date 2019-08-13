# coordinates x axis

from tkinter import *

my_window_app = Tk()

def left_Button(event):
    print('You`ve clicked on left button!', ' coordinates x axis: ', event.x, ' coordinates y axis: ', event.y)
    
def middle_Button(event):
    print('You`ve clicked on middle (scroll) button!', ' coordinates x axis: ', event.x, ' coordinates y axis: ', event.y)
        
def right_Button(event):
    print('You`ve clicked on right button!', ' coordinates x axis: ', event.x, ' coordinates y axis: ', event.y)

my_Frame = Frame(my_window_app, width = 800, height = 600)
        
my_Frame.bind('<Button-1>', left_Button)
my_Frame.bind('<Button-2>', middle_Button)
my_Frame.bind('<Button-3>', right_Button)

my_Frame.pack()

my_window_app.mainloop()
