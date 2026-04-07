import tkinter

def klik_lavy(event):
    canvas.create_text(event.x, event.y, text=1, font='Arial 30', fill='blue')

def klik_stredny(event):
    canvas.create_text(event.x, event.y, text=2, font='Arial 30', fill='green')

def klik_pravy(event):
    canvas.create_text(event.x, event.y, text=3, font='Arial 30', fill='red')

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress-1>', klik_lavy)
canvas.bind('<ButtonPress-2>', klik_stredny)
canvas.bind('<ButtonPress-3>', klik_pravy)

tkinter.mainloop()