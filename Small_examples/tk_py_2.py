import tkinter as tk

class my_App():
    def __init__(self):
        self.root = tk.Tk()
        
        level_1 = tk.Label(self.root, text = 'Hello')
        level_2 = tk.Label(self.root, text = 'World!')
        
        level_1.grid(
            row = 0, 
            column = 0, 
            padx = (100, 40),
            pady = (100, 10)
            )
        
        level_2.grid(
            row=1, 
            column=0, 
            padx=(40, 100),
            pady=(10, 100)
            ) 

app = my_App()
app.root.mainloop()