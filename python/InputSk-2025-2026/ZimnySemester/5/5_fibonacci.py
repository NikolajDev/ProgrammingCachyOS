"""
odovzdaj Napíš funkciu fibonacci(zoznam, n), ktorá dostáva nejaký aspoň dvojprvkový zoznam čísel. Do tohto zoznamu pridá ďalších n čísel tak, že každé je súčtom dvoch predchádzajúcich. Funkcia nič nevracia, len modifikuje vstupný zoznam. Napríklad:

"""

def fibonacci(zoznam, n):
    for i in range(n):
        zoznam.append(zoznam[i] + zoznam[i+1])
    
zoz = [0,-2]
print(zoz)
fibonacci(zoz, 10)
print(zoz)