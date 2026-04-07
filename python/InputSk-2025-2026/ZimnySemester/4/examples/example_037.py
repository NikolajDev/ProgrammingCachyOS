import tkinter

sirka = int(input('šírka plochy: '))

canvas = tkinter.Canvas(width=sirka)
canvas.pack()

x = 5
a = 10
while x + a < sirka:
    canvas.create_rectangle(x, 200, x + a, 200 - a, fill='white')
    x += a
    a += 10
# príkazy za cyklom

tkinter.mainloop()