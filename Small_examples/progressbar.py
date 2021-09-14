import tkinter as tk
from tkinter import ttk

def change():
    p.step(20)
    root.after(100, change) # run again after 100ms,

root = tk.Tk()

p = ttk.Progressbar(root, mode='determinate')
p.pack()

change() # run first time 

root.mainloop()
