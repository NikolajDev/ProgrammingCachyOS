sucet = 0
while True:
    retazec = input('zadaj číslo: ')
    if retazec == '':
        break
    sucet += int(retazec)
print('súčet prečítaných čísel =', sucet)