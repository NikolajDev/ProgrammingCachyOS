'''
Napíš program s funkciou pyramida(x, y), ktorá nakreslí pyramídu z kvádrov (obdĺžnikov) veľkosti: 200x50, 150x50, 100x50 a 50x50. Najväčší z nich má stred dolnej hrany (x, y), napríklad (180, 250). Všetky zafarbi štyrmi rôznymi odtieňmi zelenej. Na kreslenie použi jeden for-cyklus, v ktorom premenná cyklu farba, bude nadobúdať 4 rôzne reťazce (mená farieb) a v cykle sa budú meniť premenné y a momentálna sirka kvádra. Pre pyramida(180, 250) by si mal dostať podobný výstup:

'''
from tkinter import Canvas, mainloop

canvas = Canvas()
canvas.pack()

def pyramida(x, y):
    s1, s2, s3, s4 = 200, 150, 100, 50
    c1, c2, c3, c4 = "dark green", "green", "lime green", "lime"
    for _ in range(4):
        canvas.create_rectangle(x - s1/2, y, x + s1/2, y - 50, fill=c1)
        y -= 50
        c1, c2, c3, c4 = c2, c3, c4, c1
        s1, s2, s3, s4 = s2, s3, s4, s1
    
pyramida(180, 250)

mainloop()