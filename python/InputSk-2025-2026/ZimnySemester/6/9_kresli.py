"""
V strede prednášky je funkcia kresli(retazec), pomocou ktorej môžeme vytvárať nejakú kresbu zakódovanú písmenami 'svjz'. Nakresli pomocou tejto funkcie takýto obrázok:

../_images/106_c04.png
Teraz do tejto funkcie kresli(retazec) dopíš spracovanie týchto ďalších znakov:

'h' - kresliace pero sa bude odteraz pohybovať bez kreslenia (pero hore)

'd' - kresliace pero bude odteraz pri pohybe kresliť (pero dole)

číslice od '1' do '9' - nasledovný príkaz (jeden z 'svjz') sa vykoná príslušný počet krát

napríklad:

kresli('4v4j4z4sh5vd' * 5)
nakreslí vedľa seba 5 štvorcov:

"""


import tkinter

def kresli(canvas, retazec):
    x, y = 10, 100
    pero_dole = True
    DIGITS = '0123456789'
    n = 1
    for znak in retazec:
        x1, y1 = x, y
        if znak in DIGITS:
            n = int(znak)
        else:
            if znak == 's':
                y1 -= 10 * n
            elif znak == 'v':
                x1 += 10 * n
            elif znak == 'j':
                y1 += 10 * n
            elif znak == 'z':
                x1 -= 10 * n
            elif znak == 'h':
                pero_dole = False
            elif znak == 'd':
                pero_dole = True
            else:
                print(f'nerozumiem "{znak}"')
                return
        if pero_dole:
            canvas.create_line(x, y, x1, y1)
        x, y = x1, y1

if __name__ == "__main__":
    canvas = tkinter.Canvas()
    canvas.pack()

    kresli(canvas, '4v4j4z4sh5vd' * 5)

    tkinter.mainloop()