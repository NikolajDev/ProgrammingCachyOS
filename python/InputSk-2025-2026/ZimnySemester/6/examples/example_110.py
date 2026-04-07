t = open('subor.txt', 'r')
while True:
    riadok = t.readline()
    if riadok == '':
        break
    print(riadok, end='')
t.close()