for a in range(5, 5 * n + 1, 5):
    canvas.create_rectangle(x - a, y - a, x + a, y + a, fill=farba1)
    farba1, farba2, farba3 = farba2, farba3, farba1