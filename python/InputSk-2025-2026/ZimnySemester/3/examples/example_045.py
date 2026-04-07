import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

x, y = 10, 120

for i in range(37):
    canvas.create_oval(x-3, y-3, x+3, y+3, fill='red')
    x += 10
    y += random.randint(-10, 10)

tkinter.mainloop()