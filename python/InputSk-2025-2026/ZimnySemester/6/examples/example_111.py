t = open('subor.txt', 'r')
riadok = t.readline()
while riadok != '':
    print(repr(riadok))
    riadok = t.readline()
t.close()