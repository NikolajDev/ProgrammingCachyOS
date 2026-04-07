import tkinter
import random

def kresli():
    x = random.randint(10, 370)
    y = random.randint(10, 250)
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')
    canvas.after(100, kresli)

def kresli1():
    x = random.randint(10, 370)
    y = random.randint(10, 250)
    canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill='blue')
    canvas.after(300, kresli1)

canvas = tkinter.Canvas()
canvas.pack()

kresli()
kresli1()

tkinter.mainloop()