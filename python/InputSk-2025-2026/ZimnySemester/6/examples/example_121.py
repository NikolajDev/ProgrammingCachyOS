t = open('subor.txt', 'r')
cely_subor = ''
for riadok in t:
    cely_subor += riadok
t.close()
print(cely_subor, end='')