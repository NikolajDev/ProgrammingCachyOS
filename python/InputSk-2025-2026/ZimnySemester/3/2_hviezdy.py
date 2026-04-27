'''
Na tmavomodré pozadie canvasu (pri volaní tkinter.Canvas() nastav bg na 'navy') funkcia hviezdy(n) nakreslí na náhodné pozície n žltých hviezdičiek (create_text) znak '*' - skús ich kresliť rôznymi veľkosťami fontu (napr. veľkosť fontu nech je náhodne číslo od 10 do 20). Napríklad, pre hviezdy(200) môžeš dostať niečo podobné:
'''

from tkinter import Canvas, mainloop
import random

canvas = Canvas(width=600, height=400, bg='navy')
canvas.pack()

def stars(n):
    for _ in range(n):
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        size = random.randint(10, 20)
        canvas.create_text(x, y, text='*', fill='yellow', font=f'Arial {size}')

# Example usage
stars(2000)

mainloop()