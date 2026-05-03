"""
Budem hrať takúto hru: kladiem vedľa seba do radu mince s náhodnými hodnotami z <1, 4>; skončím, keď ich súčet bude väčší alebo rovný danému parametru hranica. Ak skončil so súčtom, ktorý je rovný hranica, vypíše text 'HURÁ' inak 'ŠKODA'. Napíš funkciu hra(n, hranica=21), ktorý túto hru odsimuluje n-krát a vypíše to pod seba, napríklad pre hra(10, 21) môžeš dostať takýto výpis:

1 2 4 4 4 1 1 2 1 3 ... ŠKODA
2 3 4 3 1 1 3 4 ... HURA
4 4 4 2 1 3 2 3 ... ŠKODA
3 4 3 1 4 1 2 1 4 ... ŠKODA
3 1 3 3 3 4 3 3 ... ŠKODA
3 4 3 1 3 2 1 2 1 2 ... ŠKODA
4 3 3 1 4 1 4 3 ... ŠKODA
4 1 1 3 4 1 2 4 1 ... HURA
3 3 2 4 1 4 1 1 4 ... ŠKODA

"""

from random import randrange

def hra(n, hranica=21):
    for i in range(n):
        sum = 0
        while sum < hranica:
            rand_num = randrange(1,5)
            sum += rand_num
            print(rand_num,end=" ")
        if sum == hranica:
            print("... HURA")
        else:
            print("... ŠKODA")

hra(10, 21)
    