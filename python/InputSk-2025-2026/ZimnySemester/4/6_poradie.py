"""
odovzdaj Napíš funkciu poradie(a, b, c), ktorá dostáva tri celá čísla a vráti ich v tvare znakového reťazca, v ktorom budú tieto čísla usporiadané od najmenšieho po najväčšie, medzi číslami bude ' <= ' Napríklad:

"""

def poradie(a,b,c):
    if a <= b <= c:
        return f"{a} <= {b} <= {c}"
    elif a <= c <= b:
        return f"{a} <= {c} <= {b}"
    elif b <= a <= c:
        return f"{b} <= {a} <= {c}"
    elif b <= c <= a:
        return f"{b} <= {c} <= {a}"
    elif c <= b <= a:
        return f"{c} <= {b} <= {a}"
    else:
        return f"{c} <= {a} <= {b}"

