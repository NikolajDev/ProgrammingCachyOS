import tkinter

def klik(event):
    farba = ['blue', 'green', 'red'][event.num-1]
    canvas.create_text(event.x, event.y, text=event.num, font='Arial 30', fill=farba)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)

tkinter.mainloop()