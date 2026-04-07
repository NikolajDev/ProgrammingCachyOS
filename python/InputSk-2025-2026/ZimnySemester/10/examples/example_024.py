import tkinter

def kresli_text(tab):
    d = 20
    for r, riadok in enumerate(tab):
        for s, prvok in enumerate(riadok):
            canvas.create_text(s * d + 10, r * d + 10, text=prvok)