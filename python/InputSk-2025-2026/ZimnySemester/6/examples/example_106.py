t = open('subor.txt', 'r')

for i in range(5):
    riadok = t.readline()
    print(riadok)

t.close()