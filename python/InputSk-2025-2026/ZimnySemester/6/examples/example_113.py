t = open('subor.txt', 'r')
riadok = t.readline()
while riadok:
    print(repr(riadok.strip()))
    riadok = t.readline()
t.close()