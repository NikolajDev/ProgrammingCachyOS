def zisti(zoznam):
    while True:
        try:
            print('prvok zoznamu =', zoznam[int(input('zadaj index: '))])
            break
        except (ValueError, IndexError):
            print('*** chybne zadany index zoznamu ***')