def cislo():
    while True:
        vstup = input('zadaj cislo: ')
        try:
            return int(vstup)
        except ValueError:
            print('*** chybne zadane cele cislo ***')