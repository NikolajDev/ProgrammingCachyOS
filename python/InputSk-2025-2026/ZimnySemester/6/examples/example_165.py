import tkinter
import random

zoz = []

def klik(event):
    global poly
    zoz[:] = [event.x, event.y]
    farba = f'#{random.randrange(256**3):06x}'
    poly = canvas.create_polygon(0, 0, 0, 0, fill=farba)

def tahaj(event):
    zoz.extend([event.x, event.y])
    canvas.coords(poly, zoz)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<B1-Motion>', tahaj)

tkinter.mainloop()