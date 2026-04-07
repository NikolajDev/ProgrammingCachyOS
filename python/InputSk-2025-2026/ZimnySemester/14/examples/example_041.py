def cislo():
    pokus = 0
    while True:
        try:
            return int(input('zadaj cislo: '))
        except ValueError:
            pokus += 1
            if pokus >= 3:
                raise
            print('*** chybne zadane cele cislo ***')