# universal_tkinter_window_with_button

import os
import tkinter as tk

root = tk.Tk()

canvas_1 = tk.Canvas(root, width = 300, height = 350, bg = 'lightsteelblue2', relief = 'raised')
canvas_1.pack()

label_1 = tk.Label(root, text = 'This is Your label', bg = 'lightsteelblue2')
label_1.config(font = ('helvetica', 20))
canvas_1.create_window(150, 80, window = label_1)


def yourCommand():
    #os.system('start cmd /k Write your COMMAND HERE AND DELETE # and pass command below')
    pass
button_1 = tk.Button(text = ' YOUR COMMAND HERE ', command = yourCommand, bg = 'green', fg = 'white', font = ('helvetica', 12, 'bold'))
canvas_1.create_window(150, 180, window = button_1)

root.mainloop()

