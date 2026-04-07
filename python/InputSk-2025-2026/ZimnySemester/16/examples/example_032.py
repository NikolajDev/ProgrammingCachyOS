def kontrola(hodnota, bola=set()):
    if hodnota in bola:
        print(hodnota, 'uz bola')
    else:
        bola.add(hodnota)
        print(hodnota, 'OK')