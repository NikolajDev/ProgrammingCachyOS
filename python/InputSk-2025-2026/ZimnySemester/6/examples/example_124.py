t = open('subor.txt', 'r')
zoznam = []
for riadok in t:
    zoznam.append(riadok)
t.close()
print(zoznam)