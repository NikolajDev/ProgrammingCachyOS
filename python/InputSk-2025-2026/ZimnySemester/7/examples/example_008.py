def vypis():
    text = vstup.get()    #'PYTHON'
    x = random.randrange(50, 330)
    y = random.randrange(20, 240)
    canvas.create_text(x, y, text=text, font='arial 20')