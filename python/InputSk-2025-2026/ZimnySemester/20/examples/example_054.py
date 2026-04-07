from PIL import Image, ImageTk
import tkinter

canvas = tkinter.Canvas(bg='green')
canvas.pack()

zoz = []
gif = Image.open('vtak.gif')
for i in range(gif.n_frames):
    gif.seek(i)
    zoz.append(ImageTk.PhotoImage(gif.convert('RGBA'))

tk_id = canvas.create_image(200, 150)
i = 0
while True:
    canvas.itemconfig(tk_id, image=zoz[i])
    i = (i + 1) % len(zoz)
    canvas.update()
    canvas.after(30)