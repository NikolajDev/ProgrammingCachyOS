def kresli_kruh(kruh):
    canvas.create_oval(kruh.x-kruh.r, kruh.y-kruh.r,
                       kruh.x+kruh.r, kruh.y+kruh.r,
                       fill=kruh.farba)