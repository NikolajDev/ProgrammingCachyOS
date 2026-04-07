import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = 100, 150
b = 280, 210
c = 170, 40

canvas.create_line(a, b)
canvas.create_line(b, c)
canvas.create_line(c, a)

tkinter.mainloop()