import tkinter

def pohyb():
    canvas.move(auto1, 4, 0)
    canvas.move(auto2, -5, 0)
    canvas.after(30, pohyb)

canvas = tkinter.Canvas(width=600)
canvas.pack()

obr_auto1 = tkinter.PhotoImage(file='auto1.png')
obr_auto2 = tkinter.PhotoImage(file='auto2.png')

auto1 = canvas.create_image(0, 150, image=obr_auto1)
auto2 = canvas.create_image(600, 150, image=obr_auto2)

pohyb()

tkinter.mainloop()