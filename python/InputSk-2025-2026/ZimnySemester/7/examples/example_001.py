import tkinter
import random

def vypis():
    text = 'PYTHON'
    x = random.randrange(50, 330)
    y = random.randrange(20, 240)
    canvas.create_text(x, y, text=text, font='arial 20')

canvas = tkinter.Canvas()
canvas.pack()

for i in range(10):
    vypis()

tkinter.mainloop()