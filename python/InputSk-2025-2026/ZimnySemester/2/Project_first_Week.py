'''
Funkcia scitaj(n) si postupne zo vstupu vypýta (pomocou input) n celých čísel a vráti znakový reťazec s načítanými číslami a ich súčtom. Parameter n má hodnotu väčšiu ako 0. Napríklad:

x = scitaj(3)
    Zadaj 1. cislo: 123
    Zadaj 2. cislo: 9
    Zadaj 3. cislo: 24
x
    '123 + 9 + 24 = 156'
Funkciu input používaj v celom skripte iba v tele tejto funkcie.
'''

def scitaj(n):
    result = 0
    str_result = ""
    for i in range(1, n):
        cislo = int(input(f"Zadaj {i}. cislo: "))
        str_result += f'{cislo} + '
        result += cislo
    cislo = int(input(f"Zadaj {n}. cislo: "))
    str_result += f'{cislo} + '
    result += cislo
    str_result += f'= {result}'
    return str_result

x = scitaj(3)
print(x)

'''
Funkcia fibonacci_medzi(od, do) vráti znakový reťazec so zoznamom fibonacciho čísel ale iba z otvoreného intervalu <od, do) (podobne ako range). Napríklad:

y = fibonacci_medzi(0, 6)
y
    '0 1 1 2 3 5 '
fibonacci_medzi(10, 14)
    '55 89 144 233 '
fibonacci_medzi(100, 101)
    '354224848179261915075 '
'''

def fibonacci(n):
    f1, f2 = 0, 1
    for _ in range(n):
        f1, f2 = f2, f1 + f2
    return f1

def fibonacci_medzi(od, do):
    result = ''
    for i in range(od, do):
        result += f"{fibonacci(i)} "
    return result

print(fibonacci_medzi(10, 14))

'''
Funkcia tabulka(n, start) vráti znakový reťazec s trojuholníkovou tabuľkou čísel v šestnástkovej sústave. Čísla sa do tabuľky dopĺňajú pstupne od štartovacieho čísla start a tabuľka sa skladá z n riadkov, pričom v prvom je n čísel a každý ďalší má o jedno číslo menej. Na vytváranie 16-ových čísel použi formátovanie f'{cislo:03x}' (môžeš si pozrieť dokumentáciu o formátovacích parametroch). Parameter n má hodnotu väčšiu ako 0. Napríklad:

z = tabulka(4, 8)
z
    '008 009 00A 00B\n    00C 00D 00E\n        00F 010\n            011'
print(z)
    008 009 00A 00B
        00C 00D 00E
            00F 010
                011
print(tabulka(7, 240))
    0F0 0F1 0F2 0F3 0F4 0F5 0F6
        0F7 0F8 0F9 0FA 0FB 0FC
            0FD 0FE 0FF 100 101
                102 103 104 105
                    106 107 108
                        109 10A
                            10B
'''

def tabulka(n, start):
    val = start
    result = ''
    for i in range(n):
        result += " "*(4*i)
        for j in range(n - i):
            result += f"{val:03X} "
            val += 1
        result += '\n'
    return result

print(tabulka(7, 240))