import tkinter

canvas = tkinter.Canvas()
canvas.pack()
tk_img = tkinter.PhotoImage(file='pyton.png')
canvas.create_image(200, 150, image=tk_img)