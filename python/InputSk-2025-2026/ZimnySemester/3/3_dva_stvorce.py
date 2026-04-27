'''
Napíš program s funkciou dva_stvorce(x, y, a1, a2), ktorá najprv nakreslí dva štvorce: prvý štvorec má ľavý horný roh (x, y) a veľkosť strany a1. Druhý štvorec má rovnaký stred ale veľkosť a2 (menšiu od a1). Potom postupne:

zafarbí ich na niektorý odtieň červenej a bledomodrej (napríklad 'indian red' a 'light blue')

k vrcholom vonkajšieho štvorca pripíše pomenovania A, B, C, D

k pravej zvislej hrane väčšieho štvorca pripíše veľkosť tohto štvorca

k spodnej hrane menšieho štvorca pripíše veľkosť tohto menšieho štvorca

Malo by to fungovať pre rôzne hodnoty parametrov.
'''

from tkinter import Canvas, mainloop

canvas = Canvas(width=500, height=500)
canvas.pack()

# Our expectations or conditions:
# The user will enter the valid x and y from the range (0,0 to 500, 500)
# Also the size of the square would not be bigger than the canvas

def dva_stvorce(x:int ,y:int ,a1:int ,a2:int):
    help = (a1 - a2)/2
    print(help)
    canvas.create_rectangle(x, y, x + a1, y + a1, 
    fill='indian red')
    canvas.create_text(x - 5, y - 5, text='A')
    canvas.create_text(x - 5, y + 5 + a1, text='D')
    canvas.create_text(x + a1 + 5, y - 5, text='B')
    canvas.create_text(x + a1 + 5, y + a1 + 5, text='C')
    canvas.create_text(x + a1 + 15, y + (a1/2), text=f"{a1}")
    x = x + help
    y = y + help
    canvas.create_rectangle(x, y, x + a2, y + a2, fill='light blue')
    canvas.create_text(x + (a2/2), y + (a2) - 10, text=f"{a2}")

dva_stvorce(50, 50, 180, 100)
mainloop()