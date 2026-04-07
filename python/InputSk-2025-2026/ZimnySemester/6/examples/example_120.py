t = open('subor.txt', 'r')
for riadok in t:
    print(repr(riadok))
    t.readline()
t.close()