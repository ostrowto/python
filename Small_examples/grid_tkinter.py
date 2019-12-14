# grid_tkinter.py

from tkinter import *

root = Tk()
root.title('Grid Tkinter Python Example')
root.geometry('960x720')



# I. Declare labels
my_Label_1 = Label(root, text = 'This is first label', bg = 'Red')
my_Label_2 = Label(root, text = 'This is second label', foreground = 'Blue')
my_Label_3 = Label(root, text = 'This is third label')

# Labels to grid
my_Label_1.grid(row = 0, column = 0)
my_Label_2.grid(row = 0, column = 1)
my_Label_3.grid(row = 0, column = 2)

# Create buttons

my_Button_1 = Button(
    root, 
    text = 'Click me! \n This is my_Button_1', 
    bg = 'Green', 
    foreground = 'White',
    padx = 100,
    pady = 100
    )

my_Button_2 = Button(
    root, 
    text = 'Click me! \n This is my_Button_2', 
    bg = 'Grey', 
    foreground = 'White',
    padx = 100,
    pady = 100
    )


my_Button_3 = Button(
    root, 
    text = 'Click me! \n This is my_Button_3', 
    bg = 'Purple', 
    foreground = 'White',
    padx = 100,
    pady = 100
    )

my_Button_4 = Button(
    root, 
    text = 'Click me! \n This is my_Button_4', 
    bg = 'Yellow', 
    foreground = 'black',
    padx = 100,
    pady = 100
    )

my_Button_5 = Button(
    root, 
    text = 'Click me! \n This is my_Button_5', 
    bg = 'Aquamarine', 
    foreground = 'White',
    padx = 100,
    pady = 100
    )

my_Button_6 = Button(
    root, 
    text = 'Click me! \n This is my_Button_6', 
    bg = 'darkgreen', 
    foreground = 'White',
    padx = 100,
    pady = 100
    )


my_Button_1.grid(row = 1, column = 0)
my_Button_2.grid(row = 1, column = 1)
my_Button_3.grid(row = 1, column = 2)
my_Button_4.grid(row = 2, column = 0)
my_Button_5.grid(row = 2, column = 1)
my_Button_6.grid(row = 2, column = 2)

root.mainloop()
