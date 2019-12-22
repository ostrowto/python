#viewer.py

from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('This is my title!')
root.iconbitmap('C:\\Users\\ostro\\Desktop\\my.ico')


my_img_1 = ImageTk.PhotoImage(Image.open('C:\\Users\\ostro\\Pictures\\wawel_1.png'))
my_img_2 = ImageTk.PhotoImage(Image.open('C:\\Users\\ostro\\Pictures\\wawel_2.png'))
my_img_3 = ImageTk.PhotoImage(Image.open('C:\\Users\\ostro\\Pictures\\wawel_3.png'))
my_img_4 = ImageTk.PhotoImage(Image.open('C:\\Users\\ostro\\Pictures\\wawel_4.png'))
my_img_5 = ImageTk.PhotoImage(Image.open('C:\\Users\\ostro\\Pictures\\wawel_5.png'))

image_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]




my_label = Label(image = my_img_1)
my_label.grid(row = 0, column = 0, columnspan = 3)


def forward_f(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(root, text = '>>', command = lambda: forward_f(image_number + 1))
    button_back = Button(root, text = '<<', command = lambda: back_f(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text='>>', state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

def back_f(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(root, text = '>>', command = lambda: forward_f(image_number + 1))
    button_back = Button(root, text = '<<', command = lambda: back_f(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text = '<<', state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)


button_back = Button(root, text = '<<', command = back_f, state = DISABLED)
button_exit = Button(root, text = 'Exit Program', command = root.quit)
button_forward = Button(root, text = '>>', command = lambda: forward_f(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)


root.mainloop()
