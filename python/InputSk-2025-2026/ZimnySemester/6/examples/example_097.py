import tkinter

def kresli(retazec):
    x, y = 100, 100
    for znak in retazec:
        x1, y1 = x, y
        if znak == 's':
            y1 -= 10
        elif znak == 'v':
            x1 += 10
        elif znak == 'j':
            y1 += 10
        elif znak == 'z':
            x1 -= 10
        else:
            print(f'nerozumiem "{znak}"')
            return
        canvas.create_line(x, y, x1, y1)
        x, y = x1, y1

canvas = tkinter.Canvas()
canvas.pack()

kresli('ssvvjjzz')

tkinter.mainloop()