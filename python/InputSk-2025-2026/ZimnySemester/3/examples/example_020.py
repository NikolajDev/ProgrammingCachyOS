import tkinter

canvas = tkinter.Canvas()
canvas.pack()

y = 100
farba1, farba2 = '#ffc0cb', '#006400'
for x in range(10, 350, 30):
    canvas.create_rectangle(x, y, x + 25, y + 50, fill=farba1)
    farba1, farba2 = farba2, farba1

tkinter.mainloop()