import tkinter
import random

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def stvorec(strana, x, y, farba=''):
    canvas.create_rectangle(x, y, x + strana, y + strana, fill=farba)

canvas = tkinter.Canvas()
canvas.pack()

for y in range(5, 230, 30):
    for x in range(5, 350, 30):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        stvorec(25, x, y, rgb(r, g, b))

tkinter.mainloop()