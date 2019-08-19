#lotto_gen_tk.py

# I. Import tkinter and random
import random
from tkinter import *

# II. Declare main frame
my_random = Tk()
my_random.geometry('600x220')
frame = Frame(my_random)
frame.pack(side = 'top')
my_random.title('1 - 49 Number Generator')

# III. Declare main function
def random_Numbers():
    ra_1 = random.randint(1, 49)
    ra_2 = random.randint(1, 49)
    ra_3 = random.randint(1, 49)
    ra_4 = random.randint(1, 49)
    ra_5 = random.randint(1, 49)
    ra_6 = random.randint(1, 49)

    num_1.set(ra_1)
    num_2.set(ra_2)
    num_3.set(ra_3)
    num_4.set(ra_4)
    num_5.set(ra_5)
    num_6.set(ra_6)
    return

# IV. Prepare to fill values into the gap
num_1 = StringVar()
num_2 = StringVar()
num_3 = StringVar()
num_4 = StringVar()
num_5 = StringVar()
num_6 = StringVar()

# V. Declare main variable
var = StringVar()
var.set('1 - 49 Number Generator')

# VI. Create frame 1
frame_1 = Frame(my_random)
frame.pack(side = 'top')

# VII. Create label
label = Label(frame_1, textvariable = var, font = ('Arial', 24), width = 24)
label.pack(side = 'top')

# VIII. Create frame 2
frame_2 = Frame(my_random)
frame_2.pack(side = 'top')

# VIII. Display randomized values into the gaps
txtDisplay = Entry(frame_2, textvariable = num_1, bd = 4, insertwidth = 1, font = ('Arial', 30, 'bold'), justify = 'center', width = 4, fg = 'red')
txtDisplay.pack(side = 'left')
txtDisplay = Entry(frame_2, textvariable = num_2, bd = 4, insertwidth = 1, font = ('Arial', 30, 'bold'), justify = 'center', width = 4, fg = 'green')
txtDisplay.pack(side = 'left')
txtDisplay = Entry(frame_2, textvariable = num_3, bd = 4, insertwidth = 1, font = ('Arial', 30, 'bold'), justify = 'center', width = 4, fg = 'blue')
txtDisplay.pack(side = 'left')
txtDisplay = Entry(frame_2, textvariable = num_4, bd = 4, insertwidth = 1, font = ('Arial', 30, 'bold'), justify = 'center', width = 4, fg = 'purple')
txtDisplay.pack(side = 'left')
txtDisplay = Entry(frame_2, textvariable = num_5, bd = 4, insertwidth = 1, font = ('Arial', 30, 'bold'), justify = 'center', width = 4, fg = 'darkcyan')
txtDisplay.pack(side = 'left')
txtDisplay = Entry(frame_2, textvariable = num_6, bd = 4, insertwidth = 1, font = ('Arial', 30, 'bold'), justify = 'center', width = 4, fg = 'magenta')
txtDisplay.pack(side = 'left')

# IX. Create frame 3
frame_3 = Frame(my_random)
frame_3.pack(side = 'top')

# X. Create button
button = Button(frame_3, state = DISABLED, font = ('Arial', 24), bg = 'white', fg = 'black', text = '1 - 49 Number Generator')
button.pack(side = 'top')
button = Button(frame_3, padx = 8, width = 18, pady = 8, bd = 4, font = ('Arial', 26), text = 'Click me!', bg = 'red', fg = 'white', command = random_Numbers)
button.pack(side = 'top')


my_random.mainloop()