def pocet(rad):
    zarazka = object()
    vysl = 0
    rad.enqueue(zarazka)
    while True:
        prvok = rad.dequeue()
        if prvok == zarazka:
            break
        rad.enqueue(prvok)
        vysl += 1
    return vysl