def odmoc(cislo):
    x = 0
    while x * x < cislo:
       x += 0.001
    return x