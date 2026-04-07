def cislo():
    while True:
        try:
            vysledok = int(input('zadaj cislo: '))
            break
        except ValueError:
            print('*** chybne zadane cele cislo ***')
    return vysledok