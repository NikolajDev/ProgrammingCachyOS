t = open('subor.txt', 'r')
cely = ''
for riadok in t:
    riadok = riadok.strip()
    if riadok != '':
        cely += riadok + '\n'
t.close()

t = open('subor2.txt', 'w')
t.write(cely)
t.close()