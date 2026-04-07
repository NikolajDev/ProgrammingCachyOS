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
tk_id1 = canvas.create_image(200, 120)
tk_id2 = canvas.create_image(100, 80)
tk_id3 = canvas.create_image(300, 100)
faza = 0
while True:
    canvas.itemconfig(tk_id1, image=zoz[faza])
    canvas.itemconfig(tk_id2, image=zoz[faza])
    canvas.itemconfig(tk_id3, image=zoz[faza])
    faza = (faza + 1) % len(zoz)
    canvas.update()
    canvas.after(100)