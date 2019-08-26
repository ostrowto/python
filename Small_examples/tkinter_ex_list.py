#tkinter_ex_list.py

# A listbox nested in the root window

from tkinter import *


input_value_one = int(input('Input value: '))
input_value = input_value_one + 1

root = Tk()
root.title('tkinter_ex_list.py')
root.geometry('300x200')

listbox = Listbox(root)
listbox.pack(fill=BOTH, expand=1)

for i in range(input_value):
    listbox.insert(END, str(i))

mainloop()
