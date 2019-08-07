# mouse_button_click.py Small example about mouse clicable buttons

# We need import this
from tkinter import *

# Create window
my_window_app = Tk()

# Define 3 buttons, each for other click operation
def write_acction_1(Event):
    print('This is acction after click on 1-st mouse button')

def write_acction_2(Event):
    print('This is acction after click on 2-nd mouse button (scroll)')

def write_acction_3(Event):
    print('This is acction after click on 3-th mouse button')

# Other version with "command", better is to "bind" buttons and events like below
#button_1 = Button(my_window_app, text = 'Click me!', command = wypisz)

button_1 = Button(my_window_app, text = 'Click me (1)!')
button_1.bind('<Button-1>', write_acction_1)

button_2 = Button(my_window_app, text = 'Click me (2)!')
button_2.bind('<Button-2>', write_acction_2)

button_3 = Button(my_window_app, text = 'Click me (3)!')
button_3.bind('<Button-3>', write_acction_3)

# Pack buttons
button_1.pack()
button_2.pack()
button_3.pack()

# We always need this - mainloop!
my_window_app.mainloop()
