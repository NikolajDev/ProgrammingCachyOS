def cislo():
    while True:
        vstup = input('zadaj cislo: ')
        if test_cele_cislo(vstup):
            return int(vstup)
        print('*** chybne zadane cele cislo ***')