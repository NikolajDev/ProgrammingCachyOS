import tkinter

canvas = tkinter.Canvas()
canvas.pack()

utvar = ((100, 50), (200, 120))
canvas.create_rectangle(utvar, fill='blue')
canvas.create_oval(utvar, fill='yellow')
utvar2 = list(utvar)                # z n-tice sa vyrobí zoznam
utvar2.append((170, 20))
canvas.create_polygon(utvar2, fill='red')

tkinter.mainloop()