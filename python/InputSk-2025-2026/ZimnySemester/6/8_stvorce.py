"""
Napíš funkciu stvorce(retazec, vel=60), ktorá dostáva dva parametre: veľkosť štvorca a znakový reťazec s menami farieb. Funkcia nakreslí rad farebných štvorcov veľkosti vel, ktoré budú zafarbené farbami z reťazca. Zrejme štvorcov bude toľko, koľko farieb je v reťazci. Pre takéto volanie:

stvorce('red blue purple red gold', 40)
by si mohol dostať takýto obrázok:

../_images/106_c02.png
Teraz túto funkciu zovšeobecni takto: parameter retazec môže pred každým menom farby obsahovať celé číslo, ktoré označuje veľkosť príslušného štvorca. Funkcia bude tieto štvorce kresliť vedľa seba, bude túto postupnosť štvorcov opakovať, ale len dovtedy, kým by nasledovný nevypadol z grafickej plochy (tento reťazec sa stále opakuje od začiatku). Do premennej sirka nastav nejakú šírku grafickej plochy a zavolaj funkciu, napríklad takto:

sirka = 450
canvas = tkinter.Canvas(width=sirka)
canvas.pack()

stvorce('40 red 20 blue purple 40 red 30 gold')
Mohol by si dostať takýto obrázok:

../_images/106_c03.png
Všimni si, že fialový ('purple') štvorec nemá určenú svoju veľkosť, teda sa použije náhradná veľkosť 60.

"""

# A

from tkinter import Canvas, mainloop

sirka = 450
canvas = Canvas(width=450)
canvas.pack()

# def stvorce_A(retazec, vel=60):
#     colors = retazec.split()
#     x, y = 10, 150
#     for farba in colors:
#         canvas.create_rectangle(x, y, x+vel, y + vel, fill=farba)
#         x += vel + 3
    

# stvorce_A('red blue purple red gold', 40)


# B


def stvorce_B(retazec, vel_predvolena=60):
    slova = retazec.split()
    x, y = 10, 100
    DIGITS = '0123456789'
    
    index = 0
    vel = vel_predvolena
    
    while True:
        slovo = slova[index % len(slova)]
        
        if slovo[0] in DIGITS:
            vel = int(slovo)
        else:
            farba = slovo
            if x + vel > sirka:
                break
            canvas.create_rectangle(x, y, x + vel, y - vel, fill=farba)

            x += vel + 3
            vel = vel_predvolena
            
        index += 1

# Volanie funkcie
stvorce_B('40 red 20 blue purple 40 red 30 gold')

mainloop()