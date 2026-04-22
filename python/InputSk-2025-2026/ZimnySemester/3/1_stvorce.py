'''
Napíš program s funkciou stvorce(x, y), ktorá najprv nakreslí dva štvorce vedľa seba (prvý má ľavý horný (x, y), veľkosť 100, druhý je o 10 odsunutý). Potom postupne:

zafarbí ich tak, že prvý bude červený a druhý modrý (parameter fill='...')

do stredu prvého vypíšeš text 'červený' a druhého 'modrý'

písmo oboch textov zväčšíš (napríklad parameter font='arial 20') a zafarbíš na žlto (parameter fill='...')

Ak bude volanie stvorce(50, 50), mal by si dostať takýto výstup:

Vyskúšaj spustiť aj pre iné hodnoty, napríklad stvorce(120, 10).
'''

from tkinter import Canvas, mainloop

def stvorce(x, y):
    canvas = Canvas()
    canvas.pack()

    canvas.create_rectangle(x,y,x+100, y+100, fill="red")
    canvas.create_text(x+50, y+50, text="červený",
    font='arial 20', fill='yellow')
    x += 110
    canvas.create_rectangle(x,y,x+100, y+100, fill='blue')
    canvas.create_text(x+50, y+50, text="modrý", font='arial 20', fill='yellow')

stvorce(50, 50)
stvorce(120, 10)

mainloop()