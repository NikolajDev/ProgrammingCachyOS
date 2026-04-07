from PIL import Image, ImageTk
import tkinter

canvas = tkinter.Canvas()
canvas.pack()
tk_id = canvas.create_image(200, 150)
obr1 = Image.open('pyton.png')
zoz = [ImageTk.PhotoImage(obr1.rotate(uhol, expand=True)) for uhol in range(0, 360, 10)]
i = 0
while True:
    canvas.itemconfig(tk_id, image=zoz[i])
    i = (i + 1) % len(zoz)
    canvas.update()
    canvas.after(100)