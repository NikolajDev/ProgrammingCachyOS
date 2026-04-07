def timer():
    for a in azoz:
        a.dalsia_faza()
    canvas.after(100, timer)

timer()