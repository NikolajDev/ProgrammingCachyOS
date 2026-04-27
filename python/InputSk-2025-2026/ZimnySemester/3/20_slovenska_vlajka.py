"""
Napíš program s funkciou slovenska_vlajka(x, y, sir, vys, modra='#0b4ea2', cervena='#ee1c25'), ktorá nakreslí vlajku Slovenska. V súbore sk.png je obrázok štítu so znakom:

../_images/sk.png
ktorý umiestniš (jeho stred) posunutý o 100 a 108 od ľavého horného okraja vlajky. V parametroch x, y, sir, vys je momentálna pozícia ľavého horného rohu, šírka a výška vlajky, modrá a červená farba. Pre volanie slovenska_vlajka(30, 30, 325, 216) by si mal dostať takýto výstup:

"""

from tkinter import Canvas, mainloop, PhotoImage

canvas = Canvas()
canvas.pack()

sk_erb = PhotoImage(file = "/home/nikolaj/ProgrammingCachyOS/python/InputSk-2025-2026/ZimnySemester/3/sk.png")

def slovenska_vlajka(x, y, sir, vys, modra='#0b4ea2', cervena='#ee1c25'):
    canvas.image = sk_erb
    y_copy = y
    colorh = vys / 3
    color1, color2, color3 = "white" , modra, cervena
    for i in range(3):
        canvas.create_rectangle(x, y_copy, x + sir, y_copy + colorh, fill=color1, width=0)
        color1, color2, color3 = color2, color3, color1
        y_copy += colorh
    canvas.create_rectangle(x, y, x + sir, y + vys)
    canvas.create_image(x + 100, y + 108, image=sk_erb)




slovenska_vlajka(30, 30, 325, 216)

mainloop()
