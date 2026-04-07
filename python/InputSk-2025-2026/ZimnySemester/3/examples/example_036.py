def kresli_bodku(x, y, farba='red', r=5):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba, width=0)