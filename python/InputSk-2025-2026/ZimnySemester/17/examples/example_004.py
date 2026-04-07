>>> start = time.time()         # zapamätaj si momentálny čas v premennej start
>>> # nejaký výpočet
>>> koniec = time.time()        # zapamätaj si momentálny čas v premennej koniec
>>> koniec - start              # koľko sekúnd ubehlo medzi týmito dvoma časmi
    33.83050608634949
>>> time.localtime(start)[3:6]    # čas start v tvare (hodiny, minúty, sekundy)
    (9, 7, 1)
>>> time.localtime(koniec)[3:6]   # čas koniec v tvare (hodiny, minúty, sekundy)
    (9, 7, 35)