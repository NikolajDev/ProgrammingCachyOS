"""
odovzdaj Budeme konštruovať takúto postupnosť celých čísel:

začneme zadaným číslom n

ak je párne, vydelíme ho 2

inak sa vynásobí 3 a pripočíta 1

toto sa opakuje, kým nedostaneme číslo 1

Napíš funkciu postupnost(n), ktorá pre dané štartové číslo n vráti (return) takto skonštruovanú postupnosť. Napríklad:

"""

def postupnost(n):
    if n == 1:
        return "1"
    result = f"{n}, "
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1
        result += f"{n}, "
        
    result += "1"
    return result

print(postupnost(1))