import tkinter

sirka = int(input('šírka plochy: '))

canvas = tkinter.Canvas(width=sirka)
canvas.pack()

x = 5
for a in range(10, sirka, 10):
    if x + a >= sirka:
        break
    canvas.create_rectangle(x, 200, x + a, 200 - a, fill='white')
    x += a

tkinter.mainloop()