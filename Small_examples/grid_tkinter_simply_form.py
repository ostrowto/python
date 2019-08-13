# grid_tkinter.py basic form

# We need to import tkinter

from tkinter import *

# Create a tkinter state in application (a window call)

window_of_app = Tk()
window_of_app.geometry('200x170')
window_of_app.title('Simply form')
window_of_app.update()

# Create labels

label_1 = Label(window_of_app, text = 'Surname')
label_2 = Label(window_of_app, text = 'Name')
label_3 = Label(window_of_app, text = 'Telephone')
label_4 = Label(window_of_app, text = 'Email')
label_5 = Label(window_of_app, text = 'Personal ID')

# Create entries (for input values and characters)

entry_1 = Entry(window_of_app)
entry_2 = Entry(window_of_app)
entry_3 = Entry(window_of_app)
entry_4 = Entry(window_of_app)
entry_5 = Entry(window_of_app)

# Invoke labels fields to grid

label_1.grid(row = 0, sticky = E)
label_2.grid(row = 1, sticky = E)
label_3.grid(row = 2, sticky = E)
label_4.grid(row = 3, sticky = E)
label_5.grid(row = 4, sticky = E)

# Invoke entries (input white fields)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)
entry_3.grid(row = 2, column = 1)
entry_4.grid(row = 3, column = 1)
entry_5.grid(row = 4, column = 1)

# If You need a checkbutton

check_Button_1 = Checkbutton(window_of_app, text = 'Please check the button \nif You love Python!')
check_Button_1.grid(columnspan = 2)

# Our never ending loop
window_of_app.mainloop()