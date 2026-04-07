def vypis(zoz):
    if len(zoz) == 0:
        print()
    else:
        print(zoz[0], end=' ')
        vypis(zoz[1:])