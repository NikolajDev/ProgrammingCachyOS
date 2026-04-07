def kresli(tab, d=20, farby=('black', 'yellow', 'orange', 'blue', 'red', 'white')):
    canvas.delete('all')
    for r, riadok in enumerate(tab):
        for s, prvok in enumerate(riadok):
            x, y = s * d + 5, r * d + 5
            farba = farby[prvok]
            canvas.create_rectangle(x, y, x + d, y + d,
                                    fill=farba, outline='light gray')
    canvas.update()