...

class Skupina:
    def __init__(self):
        self.zoznam = []

    def pridaj(self, utvar):
        self.zoznam.append(utvar)

canvas = tkinter.Canvas()
canvas.pack()
Kruh.canvas = Obdlznik.canvas = canvas

sk = Skupina()
sk.pridaj(Kruh(50, 50, 30, 'blue'))
sk.pridaj(Obdlznik(100, 20, 100, 50))
sk.zoznam[0].prefarbi('green')
sk.zoznam[1].posun(50)