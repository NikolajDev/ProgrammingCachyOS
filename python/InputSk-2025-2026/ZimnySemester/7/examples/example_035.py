import tkinter

x, y = 200, 200
zoznam = [x, y]

def kresli(dx, dy):
    global x, y
    x += dx
    y += dy
    zoznam.extend((x, y))
    canvas.coords(ciara, zoznam)

def udalost_vlavo(event):
    kresli(-10, 0)

def udalost_vpravo(event):
    kresli(10, 0)

def udalost_hore(event):
    kresli(0, -10)

def udalost_dolu(event):
    kresli(0, 10)

canvas = tkinter.Canvas()
canvas.pack()

ciara = canvas.create_line(0, 0, 0, 0)        # zatiaľ prázdna čiara
canvas.bind_all('<Left>', udalost_vlavo)
canvas.bind_all('<Right>', udalost_vpravo)
canvas.bind_all('<Up>', udalost_hore)
canvas.bind_all('<Down>', udalost_dolu)

tkinter.mainloop()