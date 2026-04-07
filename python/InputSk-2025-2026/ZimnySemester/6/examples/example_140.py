t = open('subor.txt', 'r')
cely = t.read()
t.close()

t = open('subor2.txt', 'w')
t.write(cely)
t.close()