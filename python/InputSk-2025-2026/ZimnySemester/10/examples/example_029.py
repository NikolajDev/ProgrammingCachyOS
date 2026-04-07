def zmen():
    for i, riadok in enumerate(t):
        for j in range(len(riadok)):
            riadok[j] += i + 1
    kresli(t)

canvas = tkinter.Canvas()
canvas.pack()
tkinter.Button(text='Zmeň', command=zmen).pack()

t = vyrob(7, 11)
ocisluj(t)
kresli(t)

tkinter.mainloop()