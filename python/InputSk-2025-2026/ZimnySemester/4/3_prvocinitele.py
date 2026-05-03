"""
odovzdaj Napíš funkciu prvocinitele(cislo), ktorá zadané číslo ** rozloží na prvočinitele** (vyjadrí ho ako súčin prvočísel). Tento rozklad vrátiš ako reťazec v tvare rovnosti s násobením:

t = prvocinitele(60)
t
    '60 = 2 * 2 * 3 * 5'
prvocinitele(1001)
    '1001 = 7 * 11 * 13'
prvocinitele(37)
    '37 = 37'

"""

def prvocinitele(n):
    if n == 1:
        return f"1 nie je prvocislo"
    result = f"{n} ="
    divider = 2
    while n != 1:
        if divider == n:
            result += f" {str(divider)}"
            n //= divider
        elif n % divider == 0:
            result += f" {str(divider)} *"
            n //= divider
        else:
            divider += 1
    return result

print(prvocinitele(60))  