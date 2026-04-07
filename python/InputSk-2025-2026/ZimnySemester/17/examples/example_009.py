def odmoc(cislo, eps=0.0001):
    pocet = 0
    od, do = 0, cislo
    x = (od + do) / 2
    while abs(x ** 2 - cislo) > eps:
        if x ** 2 > cislo:
           do = x
        else:
            od = x
        x = (od + do) / 2
        pocet += 1
    return x, pocet

x, pocet = odmoc(150000000)
print(round(x, 3), pocet)