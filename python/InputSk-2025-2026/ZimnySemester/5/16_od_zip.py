"""
Napíš funkciu od_zip(zoznam), ktorá bude fungovať ako opak funkcie moj_zip. Funkcia dostáva zoznam dvojíc a vráti dva zoznamy prvých a druhých prvkov dvojíc. Napríklad:
z1, z2 = od_zip([(2, 'a'), ('h', 3), (5, 'o'), ('j', 7)])
z1
    [2, 'h', 5, 'j']
z2
    ['a', 3, 'o', 7]
"""

def od_zip(zoznam):
    list1 = []
    list2 = []
    for tuple_ in zoznam:
        list1.append(tuple_[0])
        list2.append(tuple_[1])
    return list1, list2

z1, z2 = od_zip([(2, 'a'), ('h', 3), (5, 'o'), ('j', 7)])
print(z1)
print(z2)