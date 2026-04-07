import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

for i in range(100):
    x = random.randint(20, 380)
    y = random.randint(20, 260)
    canvas.create_line(0, 0, x, y)

tkinter.mainloop()