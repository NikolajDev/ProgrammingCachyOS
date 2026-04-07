azoz = [Anim(200, 120, zoz),
        Anim(100, 80, zoz),
        Anim(300, 100, zoz),
        Anim(150, 200, zoz)]
while True:
    for a in azoz:
        a.dalsia_faza()
    canvas.update()
    canvas.after(100)