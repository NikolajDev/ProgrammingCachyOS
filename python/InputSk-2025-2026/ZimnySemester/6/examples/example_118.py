t = open('subor.txt', 'r')
riadok = t.readline()
print('najprv som precital:', repr(riadok.rstrip()))
print('v subore ostali este tieto riadky:')
for riadok in t:
    print(repr(riadok.rstrip()))
t.close()