def pocet_prvkov(zasobnik):
    pocet = 0
    while not zasobnik.is_empty():
        zasobnik.pop()
        pocet += 1
    return pocet