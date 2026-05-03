"""
Napíš funkciu platna(x, y, r, k), ktorá nakreslí gramofónovú LP platňu ako niekoľko sústredných kružníc. Najväčšia z nich má polomer r a každá ďalšia je o 3 menšia. Najmenšia kružnica by nemala mať menší polomer ako 15. Každú k-tu kružnicu nakresli šedou farbou (začni od najväčšej). Napríklad pre volanie platna(190, 130, 120, 6) by si mal dostať takýto obrázok:

"""

from tkinter import Canvas, mainloop

canvas = Canvas()
canvas.pack()

def platna(x, y, r, k):
    index = 0
    while r >= 15:
        if index % k == 0:
            farba = "gray"
        else:
            farba = "black"
            
        canvas.create_oval(x-r, y-r, x+r, y+r, outline=farba)
        
        r -= 3
        index += 1

platna(190, 130, 120, 6)
    
mainloop()