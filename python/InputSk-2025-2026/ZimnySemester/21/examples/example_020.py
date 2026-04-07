import tkinter
import random
from PIL import Image, ImageTk

class Plocha:
    ...

class Anim:
    canvas = None
    ...

class Program:
    def __init__(self):

        def strihaj(meno_suboru, n):
            obr = Image.open(meno_suboru)
            sir, vys = obr.width // n, obr.height
            return [ImageTk.PhotoImage(obr.crop((x, 0, x + sir, vys)))
                        for x in range(0, obr.width, sir)]

        win = tkinter.Tk()
        win.title('zvieratka v lese')
        zoz1 = strihaj('vtak.png', 8)
        zoz2 = strihaj('zajo.png', 8)
        obr = Image.open('pyton.png')
        zoz3 = [ImageTk.PhotoImage(obr.rotate(uhol, expand=True)) for uhol in range(0, 360, 10)]
        obr = Image.open('kacicka.png')
        zoz4 = [ImageTk.PhotoImage(obr.resize(int(v*r) for v in obr.size))
                                   for r in (.6, .55, .5, .45, .4, .35, .3, .35, .4, .45, .5, .55)]
        Plocha('les.png', zoz1, zoz2, zoz3, zoz4)

Program()