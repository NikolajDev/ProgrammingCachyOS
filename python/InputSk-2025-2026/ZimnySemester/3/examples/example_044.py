import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = 100, 150
b = 280, 210
c = 170, 40

canvas.create_line(a, b, c, a)

canvas.create_text(a, text='A')
canvas.create_text(b, text='B')
canvas.create_text(c, text='C')

tkinter.mainloop()