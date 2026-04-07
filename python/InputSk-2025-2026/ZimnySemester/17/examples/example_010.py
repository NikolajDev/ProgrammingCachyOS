def zisti(zoznam, hodnota):
    for meno, cislo in zoznam:
        if meno == hodnota:
            return cislo
    return 'nenasiel'