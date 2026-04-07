import tkinter

def test(event):
    print(event.keysym)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind_all('<KeyPress>', test)

tkinter.mainloop()