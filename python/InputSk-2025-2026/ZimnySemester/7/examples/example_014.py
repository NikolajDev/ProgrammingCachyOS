import tkinter

def klik(event):
    print('klik', event.x, event.y)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)

tkinter.mainloop()