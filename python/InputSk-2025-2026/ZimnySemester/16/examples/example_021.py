import tkinter

def kruh(r, x, y):
    canvas.create_oval(x - r, y - r, x + r, y + r)

canvas = tkinter.Canvas()
canvas.pack()

kruh(50, 100, 100)