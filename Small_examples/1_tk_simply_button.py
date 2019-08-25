# Simply tkinter button

import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text = 'Click on me!', command = self.say_hello)
        self.btn.pack(padx=120, pady=30)

    def say_hello(self):
        print('Hello! Have a nice day!')

if __name__ == '__main__':
    app = App()
    app.title('My simply Tkinter app')
    app.mainloop()