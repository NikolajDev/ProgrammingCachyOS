def pocet_prvkov(zasobnik):
    pocet = 0
    kopia = zasobnik
    while not kopia.is_empty():
        kopia.pop()
        pocet += 1
    return pocet