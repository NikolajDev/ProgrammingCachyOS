"""
odovzdaj Športovec prvý deň prebehol x kilometrov. Každý ďalší deň prebehol o 10% viac ako v predchádzajúci deň. Napíš funkciu sportovec(x, y), ktorá pre dané y zistí, v ktorý deň športovec prebehne aspoň y kilometrov. Funkcia vráti (return) reťazec s odpoveďou, desatinné číslo vlož do výsledku pomocou {cislo:.2f}. Napríklad, po spustení môžeš dostať:

"""

def sportovec(x, y):
    semi_result = x
    day = 1
    while semi_result < y:
        semi_result *= 1.1
        day += 1
    return f"na {day}. deň prebehne {semi_result:.2f} km"
    
print(sportovec(10, 20))