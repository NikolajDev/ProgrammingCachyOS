"""
odovzdaj Napíš funkciu sucet(od, do), ktorá vypočíta súčty druhých mocnín celých čísel z intervalu <od, do>, pričom z tejto postupnosti čísel vynechá každé druhé. Napríklad pre sucty(5, 10) vypočíta súčet 5**2 + 7**2 + 9**2.
"""

def sucet(od: int, do:int):
    result = 0
    for i in range(od, do, 2):
        result += i ** 2
    return result

print(sucet(5, 10))