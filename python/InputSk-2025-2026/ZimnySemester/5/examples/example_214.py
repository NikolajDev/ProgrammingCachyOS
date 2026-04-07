utvar1 = e, a, c
utvar2 = e, d, b
utvar3 = a, b, c, d
utvar4 = a, c, d, b

for param in (utvar1, 'green'), (utvar2, 'yellow'), (utvar3, 'red'), (utvar4, 'blue'):
    utvar, farba = param
    canvas.create_polygon(utvar, fill=farba)