teploty = [10, 13, 15, 18, 17, 12, 12]

sucet = 0
for prvok in teploty:
    sucet += prvok
priemer = sucet / 7
print(f'priemerná teplota je {priemer:.1f}')    # formátovanie desatinného čísla na jedno miesto