odkial = open('subor.txt', 'r')
kam = open('subor2.txt', 'w')
for riadok in odkial:
    riadok = riadok.strip()
    if riadok != '':
        kam.write(riadok + '\n')
odkial.close()
kam.close()