import tkinter

def stvorcova_siet(n):
    canvas = tkinter.Canvas()
    canvas.pack()

    for i in range(n):
        for j in range(n):
            x = j * 20 + 100
            y = i * 20 + 12
            if i == 5:
                farba = 'red'
            else:
                farba = 'white'
            canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=farba)

    tkinter.mainloop()

stvorcova_siet(13)