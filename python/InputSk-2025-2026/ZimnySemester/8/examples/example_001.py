import tkinter

canvas = tkinter.Canvas()                        # vytvor grafickú plochu
canvas.pack()                                    # zobraz ju do okna

i = g.create_oval(100, 50, 150, 80, fill='red')  # nakresli červenú elipsu
canvas.itemconfig(i, fill='blue')                # zmeň farbu výplne elipsy

tkinter.mainloop()                               # zabezpeč grafickú aplikáciu