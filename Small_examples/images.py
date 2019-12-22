#images.py

from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('This is my title!')
root.iconbitmap('C:\\Users\\ostro\\Desktop\\my.ico')


my_img = ImageTk.PhotoImage(Image.open('C:\\Users\\ostro\\Pictures\\wawel_1.png'))
my_label = Label(image = my_img)
my_label.pack()



button_quit = Button(root, text = 'Exit Program', command = root.quit)
button_quit.pack()


root.mainloop()
