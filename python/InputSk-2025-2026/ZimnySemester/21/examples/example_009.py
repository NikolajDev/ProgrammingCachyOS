sir, vys = 1280, 817
canvas = tkinter.Canvas(width=sir, height=vys)
canvas.pack()
pozadie = tkinter.PhotoImage(file='les.png')
canvas.create_image(sir/2, vys/2, image=pozadie)