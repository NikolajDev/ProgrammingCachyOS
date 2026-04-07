import tkinter
import random

zoz = []

def klik(event):
    global poly, farba
    zoz[:] = [event.x, event.y]
    farba = f'#{random.randrange(256**3):06x}'
    poly = canvas.create_polygon(0, 0, 0, 0, fill=farba)

def tahaj(event):
    zoz.extend([event.x, event.y])
    canvas.coords(poly, zoz)

def pusti(event):
    with open('obrazok.txt', 'a') as subor:
        print(farba, ' '.join(str(i) for i in zoz), file=subor)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<B1-Motion>', tahaj)
canvas.bind('<ButtonRelease>', pusti)

tkinter.mainloop()