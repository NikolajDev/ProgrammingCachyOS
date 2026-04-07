def pocet_prvkov(zasobnik):
    pocet = 0
    kopia = Stack()                   # pomocný zásobník
    while not zasobnik.is_empty():
        kopia.push(zasobnik.pop())
        pocet += 1
    while not kopia.is_empty():       # vráti pôvodný obsah zásobníka
        zasobnik.push(kopia.pop())
    return pocet