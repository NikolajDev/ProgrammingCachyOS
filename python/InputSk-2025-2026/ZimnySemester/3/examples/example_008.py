import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

for i in range(10):
    x = random.randint(0, 380)
    y = random.randint(0, 260)
    canvas.create_text(x, y, text=(x, y))

tkinter.mainloop()