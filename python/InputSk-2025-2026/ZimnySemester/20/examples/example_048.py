from PIL import Image, ImageTk
import tkinter

canvas = tkinter.Canvas()
canvas.pack()
obr1 = Image.open('pyton.png')
obr2 = obr1.rotate(45, expand=True)
tk_img = ImageTk.PhotoImage(obr2)
canvas.create_image(200, 150, image=tk_img)