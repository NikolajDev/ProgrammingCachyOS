cislo = int(input('zadaj cislo: '))
delitele = ()
for i in range(1, cislo + 1):
    if cislo % i == 0:
        delitele = delitele + (i,)
print('delitele', cislo, 'su', delitele)