def zisti(zoznam):
    while True:
        try:
            vstup = input('zadaj index: ')
            index = int(vstup)
            print('prvok zoznamu =', zoznam[index])
            break
        except ValueError:
            print('*** chybne zadane cele cislo ***')
        except IndexError:
            print('*** index mimo rozsah zoznamu ***')