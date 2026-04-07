mx = teploty[0]
for prvok in teploty:
    if mx < prvok:
        mx = prvok
print('najteplejšie bolo', mx, 'stupňov')