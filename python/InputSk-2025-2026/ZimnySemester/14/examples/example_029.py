def cislo():
    ok = False
    while not ok:
        try:
            vysledok = int(input('zadaj cislo: '))
            ok = True
        except ValueError:
            print('*** chybne zadane cele cislo ***')
    return vysledok