from PIL import Image, ImageTk
import tkinter

canvas = tkinter.Canvas()
canvas.pack()
obr1 = Image.open('pyton.png')
tk_img = ImageTk.PhotoImage(obr1)       # konverzia z PIL.Image do tkinter
canvas.create_image(200, 150, image=tk_img)