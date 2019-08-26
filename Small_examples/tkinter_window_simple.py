# tkinter simple window


import tkinter as tk
from tkinter import messagebox

def Klik():
    global okieneczko
    odp = tk.messagebox.askquestion('Pytanko', 'Na pewno?')
    if odp == 'yes':
        okieneczko.destroy()


okieneczko = tk.Tk()
okieneczko.title('Okieneczko')
guziczek = tk.Button(okieneczko, text = 'Pa!', command = Klik)
guziczek.place(x = 50, y = 50)


okieneczko.mainloop()
