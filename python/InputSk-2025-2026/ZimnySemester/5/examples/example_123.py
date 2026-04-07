def vypis(zoznam, pocet):
    p = 0
    while zoznam:
        print(zoznam.pop(0), end=' ')
        p += 1
        if p % pocet == 0:
            print()