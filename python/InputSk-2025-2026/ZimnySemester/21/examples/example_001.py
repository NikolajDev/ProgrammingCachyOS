import tkinter
from PIL import Image, ImageTk

def strihaj(meno_suboru, n):
    obr = Image.open(meno_suboru)
    sir, vys = obr.width // n, obr.height
    return [ImageTk.PhotoImage(obr.crop((x, 0, x + sir, vys)))
                for x in range(0, obr.width, sir)]

canvas = tkinter.Canvas()
canvas.pack()

zoz = strihaj('vtak.png', 8)
tk_id = canvas.create_image(200, 150)
faza = 0
while True:
    canvas.itemconfig(tk_id, image=zoz[faza])
    faza = (faza + 1) % len(zoz)
    canvas.update()
    canvas.after(100)