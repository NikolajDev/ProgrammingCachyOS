utvar1 = e, a, c
utvar2 = e, d, b
utvar3 = a, b, c, d
utvar4 = a, c, d, b

for utvar, farba in (utvar1, 'green'), (utvar2, 'yellow'), (utvar3, 'red'),(utvar4, 'blue'):
    canvas.create_polygon(utvar, fill=farba)