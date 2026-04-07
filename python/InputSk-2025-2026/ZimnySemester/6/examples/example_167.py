import tkinter

canvas = tkinter.Canvas()
canvas.pack()

with open('obrazok.txt') as subor:
    for riadok in subor:
        riadok = riadok.split()
        # farba, zoz = riadok[0], [int(i) for i in riadok[1:]]
        # canvas.create_polygon(zoz, fill=farba)
        canvas.create_polygon([int(i) for i in riadok[1:]], fill=riadok[0])

tkinter.mainloop()