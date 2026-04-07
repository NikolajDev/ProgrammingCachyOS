import tkinter

ddef casovac():
    print('tik')
    canvas.after(1000, casovac)

canvas = tkinter.Canvas()
canvas.pack()

casovac()

tkinter.mainloop()