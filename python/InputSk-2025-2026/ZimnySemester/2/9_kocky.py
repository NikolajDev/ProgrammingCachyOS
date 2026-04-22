"""
Budeme simulovať hádzanie viacerými hracími kockami. Zakaždým vypíšeme aj ich súčet. Napíš funkciu kocky(n, pocet), ktorá to simuluje n-krát, pričom v parametri pocet je počet kociek. Môžeš dostať takýto výstup:

>>> kocky(3, 4)
    na 1. kocke padla 3
    na 2. kocke padla 2
    na 3. kocke padla 2
    na 4. kocke padla 2
    ich súčet je 9
    ======================
    na 1. kocke padla 4
    na 2. kocke padla 6
    na 3. kocke padla 1
    na 4. kocke padla 5
    ich súčet je 16
    ======================
    na 1. kocke padla 1
    na 2. kocke padla 4
    na 3. kocke padla 6
    na 4. kocke padla 3
    ich súčet je 14
    ======================
"""

from random import randint

def kocky(n, pocet):
    for i in range(n):
        result = 0
        for j in range(1, pocet+1):
            val = randint(1,6)
            print(f"na {j}. kocke padal {val}")
            result += val
        print(f"ich sucet je {result}")
        print("=" * 20)

kocky(3, 4)