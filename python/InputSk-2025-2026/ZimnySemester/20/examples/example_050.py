from PIL import Image, ImageTk
import tkinter

canvas = tkinter.Canvas()
canvas.pack()
tk_id = canvas.create_image(200, 150)     # zatiaľ prázdny obrázok

uhol = 0
while True:
    tk_img = ImageTk.PhotoImage(Image.open('pyton.png').rotate(uhol, expand=True))
    canvas.itemconfig(tk_id, image=tk_img)
    uhol += 10
    canvas.update()
    canvas.after(100)