import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def sustredne_stvorce(n, farba1='red', farba2='blue', farba3='yellow'):
    x, y = 190, 130
    for a in reversed(range(5, 5 * n + 1, 5)):
        canvas.create_rectangle(x - a, y - a, x + a, y + a, fill=farba1)
        farba1, farba2, farba3 = farba2, farba3, farba1

sustredne_stvorce(20)

tkinter.mainloop()