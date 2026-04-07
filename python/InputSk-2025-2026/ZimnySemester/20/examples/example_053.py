import tkinter
# moduly Image ani ImageTk tu nepotrebujeme

canvas = tkinter.Canvas(bg='green')
canvas.pack()
tk_id = canvas.create_image(200, 150)
zoz = [tkinter.PhotoImage(file=f'vtak/vtak{i}.png') for i in range(8)]
i = 0
while True:
    canvas.itemconfig(tk_id, image=zoz[i])
    i = (i + 1) % len(zoz)
    canvas.update()
    canvas.after(100)