def vypis1(zoz):
    if len(zoz) != 0:
        vypis1(zoz[1:])
        print(zoz[0], end=' ')

def vypis2(zoz):
    if len(zoz) != 0:
        print(zoz[0], end=' ')
        vypis2(zoz[1:])
        print(zoz[0], end=' ')