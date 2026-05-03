"""
Napíš funkciu vypis(zoznam, pocet=1), ktorá prvky daného 
zoznamu vypíše tak, že v každom riadku (možno okrem posledného) vypíše presne zadaný pocet prvkov zoznamu. Funkcia nemodifikuje vstupný zoznam. Napríklad:

"""

def vypis(zoznam, pocet=1):
    helper_counter = 0
    for i in zoznam:
        if helper_counter < pocet:
            print(i, end=" ")
            helper_counter += 1
        else:
            print()
            print(i, end=" ")
            helper_counter = 1

zoz = list(range(1, 19))
vypis(zoz, 1)
vypis(['prvy', 'druhy', 'treti'])