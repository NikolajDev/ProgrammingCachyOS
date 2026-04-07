def timer():
    for a in azoz:
        a.dalsia_faza()
    canvas.after(100, timer)

def klik(event):
    azoz.append(Anim(event.x, event.y, zoz))

canvas = tkinter.Canvas()
canvas.pack()

zoz = strihaj('vtak.png', 8)
azoz = []
timer()
canvas.bind('<ButtonPress>', klik)