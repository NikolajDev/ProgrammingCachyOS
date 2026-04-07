teploty = [10, 13, 15, 18, 17, 12, 12]

sucet = 0
for prvok in teploty:
    sucet += prvok
priemer = sucet / 7
pocet = 0
for prvok in teploty:
    if prvok > priemer:
        pocet += 1
print('počet nadpriemerne teplých dní:', pocet)