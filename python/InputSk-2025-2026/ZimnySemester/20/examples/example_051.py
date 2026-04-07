from PIL import Image, ImageTk
import tkinter

canvas = tkinter.Canvas()
canvas.pack()
tk_id = canvas.create_image(200, 150)
obr1 = Image.open('pyton.png')
uhol = 0
while True:
    tk_img = ImageTk.PhotoImage(obr1.rotate(uhol, expand=True))
    canvas.itemconfig(tk_id, image=tk_img)
    uhol += 10
    canvas.update()
    canvas.after(100)