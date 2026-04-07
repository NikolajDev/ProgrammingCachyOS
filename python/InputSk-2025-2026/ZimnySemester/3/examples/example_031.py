import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(80, 50, 300, 200)
canvas.create_oval(80, 50, 300, 200, fill='white')

tkinter.mainloop()