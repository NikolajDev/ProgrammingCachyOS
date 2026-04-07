import tkinter

class Vizualizuj:
    def __init__(self, zoz):
        self.zoz = zoz
        self.canvas = tkinter.Canvas(width=800, height=600, bg='white')
        self.canvas.pack()
        self.dx = 800 / len(zoz)
        self.id = {}
        for i in range(len(zoz)):
            self.id[i] = self.canvas.create_line(i*self.dx, 600, i*self.dx, 600-zoz[i])

    def __getitem__(self, index):
        return self.zoz[index]

    def __setitem__(self, index, hodnota):
        self.zoz[index] = hodnota
        self.canvas.coords(self.id[index], index*self.dx, 600, index*self.dx, 600-hodnota)
        self.canvas.update()

    def __len__(self):
        return len(self.zoz)