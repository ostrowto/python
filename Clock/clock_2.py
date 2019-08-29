import tkinter
import time
from datetime import datetime

# I. define clacc for clock

class my_Clock(tkinter.Label):

    def __init__(self, parent = None, seconds = True, colon = False):
        
        tkinter.Label.__init__(self, parent)
        self.display_Seconds = seconds
        if self.display_Seconds:
            self.time = time.strftime('%H:%M:%S')
        else:
            self.time = time.strftime('%I:%M %p').lstrip('0')
        self.display_Time = self.time
        self.configure(text = self.display_Time)
        self.after(200, self.seconds_time)

    def seconds_time(self):
        if self.display_Seconds:
            new_time = time.strftime('%H:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_Time = self.time
            self.config(text = self.display_Time)
        self.after(200, self.seconds_time)

# II. Define a date
filename_datetime = datetime.now().strftime("\n\n\tDate: %Y-%m-%d Clock opening: %H:%M:%S")

# III. Create a tkinter window
if __name__ == "__main__":
   
    root = tkinter.Tk()
    root.title(filename_datetime)
    root.lift()
    root.attributes('-topmost', True)
    root.geometry('390x160')
    root.resizable(False, False)
    root.configure(bg = 'light blue')
    main_frame  = tkinter.Frame(root)
    main_frame.pack()
 
    tkinter.Label(main_frame, text='Enjoy the time!').pack()

    clock = my_Clock(main_frame)
    clock.pack()
    clock.configure(bg = 'darkblue', fg = 'white', font = ("arial", 70))

    tkinter.Label(main_frame, text='Remember time is money!').pack()
   
    root.mainloop()