# app.py by Dev Ed https://www.youtube.com/watch?v=jE-SpRI3K5g&feature=youtu.be 

import tkinter as tk
from tkinter import filedialog, Text
import os

# We define root
root = tk.Tk()
apps = []

# We need this for split results in the saving file
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

# First function
def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir = '/', title = 'Select File', filetypes = (('executables', '*.exe'), ('all files', '*.*')))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = 'gray')
        label.pack()

# Seccond function
def runApps():
    for app in apps:
        os.startfile(app)

# Some canvas, frames and buttons
canvas = tk.Canvas(root, height = 700, width = 700, bg = '#263D42')
canvas.pack()

frame = tk.Frame(root, bg = 'white')
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = 'Open File', padx = 10, pady = 5, fg = 'white', bg = '#263D42', command = addApp)
openFile.pack()

runApps = tk.Button(root, text = 'Run Apps', padx = 10, pady = 5, fg = 'white', bg = '#263D42', command = runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

# We save our exaples in to the simply text file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
