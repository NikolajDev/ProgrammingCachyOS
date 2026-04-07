def kresli_text(text):
    x = random.randint(50, 330)
    y = random.randint(20, 240)
    canvas.create_text(x, y, text=text)

kresli_text('PYTHON')