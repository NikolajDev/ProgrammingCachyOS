"""
Unicode 0x2654 a ďalších päť za ním sú obrázky šachových figúrok. Napíš program, ktorý do grafickej plochy nakresli vedľa seba všetkých 6 figúrok náhodnými farbami väčším fontom (napríklad 'arial 50'). Môžeš dostať takýto obrázok:

"""

from tkinter import Canvas, mainloop
from random import randrange

canvas = Canvas()
canvas.pack()

def random_color():
    return f"#{randrange(256**3):06x}"

x = 30
y = 150

start = 0x2654
for i in range(6):
    canvas.create_text(x, y, text=f"{chr(start + i)}", fill=random_color(), font=('Segoe UI Symbol', 50))
    x += 60
    



mainloop()