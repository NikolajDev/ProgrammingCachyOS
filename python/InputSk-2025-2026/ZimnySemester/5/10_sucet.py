"""
odovzdaj Napíš funkciu sucet(zoznam1, zoznam2), ktorá sčíta/zlepí dva zoznamy čísel/reťazcov po prvkoch. Tieto zoznamy môžu byť rôzne dlhé. Funkcia vráti (return) nový zoznam. Napríklad:

"""

def sucet(zoznam1, zoznam2):
    max_ = []
    min_ = []
    if len(zoznam1) < len(zoznam2):
        max_ = zoznam2
        min_ = zoznam1
    else:
        max_ = zoznam1
        min_ = zoznam2
    for i in range(len(min_)):
        max_[i] = max_[i] + min_[i]
    return max_
    

print(sucet(['1.', '2.', '3.', '4.'], list('python')))