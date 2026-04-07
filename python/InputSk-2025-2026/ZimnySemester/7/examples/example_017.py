import tkinter
import random

def klik(event):
    x, y = event.x, event.y
    for r in range(50, 0, -5):
        farba = f'#{random.randrange(256**3):06x}'
        canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)

tkinter.mainloop()