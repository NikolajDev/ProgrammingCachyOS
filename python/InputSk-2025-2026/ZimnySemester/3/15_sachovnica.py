"""
Napíš program s funkciou sachovnica(pr, ps, vel, farba1, farba2), ktorá nakreslí farebnú šachovnicu. V parametroch pr, ps, vel, farba1, farba2 dostáva počet stĺpcov, počet riadkov, veľkosť štvorčeka a dve farby, ktoré sa majú na šachovnici striedať. Medzi nakreslenými štvorčekmi je ešte medzera veľkosti 3. Pre volanie sachovnica(6, 10, 30, 'maroon', 'gold') môžeš dostať takýto výstup:

"""

from tkinter import Canvas, mainloop

canvas = Canvas()
canvas.pack()

def sachovnica(pr, ps, vel, farba1, farba2):
    x = 5
    y = 5
    for i in range(pr):
        for j in range(ps):
            canvas.create_rectangle(x, y, x + vel, y + vel, fill=farba1)
            farba1, farba2 = farba2, farba1
            x += vel + 3
        y += vel + 3
        x = 5
        farba1, farba2 = farba2, farba1

sachovnica(6, 10, 30, 'maroon', 'gold')

mainloop()
    