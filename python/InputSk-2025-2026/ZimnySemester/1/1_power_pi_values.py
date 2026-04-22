"""
Pomocou operácie ** vieme vypočítať mocniny čísel. Ak je exponentom, napríklad zlomok 1/2 (alebo desatinné číslo 0.5), tak vypočítame druhú odmocninu čísla. Zapíš v Pythone:
    do premennej a1 priraď druhú odmocninu z 3
    do premennej a2 priraď tretinu tretej odmocniny z 5
    do premennej a3 priraď piatu mocninu piatej odmocniny z 1024
    do premennej a4 priraď desiatu odmocninu z dvadsiatej mocniny 2
Hodnoty týchto štyroch premenných potom vypíš v tvare:
"""

a1 = 3 ** (1/2)
print(a1)
a2 = (5 ** (1/3)) / 3
print(a2)
a3 = (1024 ** (1/5)) ** 5
print(a3)
a4 = (2 ** 20) ** (1/10)

"""
predpokladaj, že
pi = 3.141592653589793
zisti (len pomocou výpisov), ktorý zo vzorcov sa k tomuto číslu pi priblížil najviac:
    pi1 = podiel 223 a 71
    pi2 = súčet zlomkov 22/17, 37/47 a 88/83
    pi3 = druhá mocnina 99 lomeno súčin 2206 krát druhá odmocnina z 2
    pi4 = druhá odmocnina z 5, k tomu plus 6, to celé druhá odmocnina, k tomu plus 7 a to celé opäť druhá odmocnina
    pi5 = 10 na 100 lomeno 11222.11122 a to celé 193-tia odmocnina
Napríklad podiel 223 a 71 sa od pi líši o 0.0007475831672580924, preto výpis môže vyzerať takto:
pi1 = 3.140845070422535
rozdiel = 0.0007475831672580924
"""

PI = 3.141592653589793

pi1 = 223/71
diff1 = PI - pi1    # sktdiff = 0.0007475831672580924
print(f"pi = {pi1}\ndiff = {diff1}")
pi2 = (22 / 17) + (37 / 47) + (88 / 83)
diff2 = PI - pi2    # diff = 1.2235634727630895e-10
print(f"pi = {pi2}\ndiff = {diff2}")
pi3 = (99 ** 2) /  2206 * (2 ** (1/2))
diff3 = PI - pi3    # diff = -3.141592806436819
print(f"pi = {pi3}\ndiff = {diff3}")
pi4 = (((5 ** (1/2)) + 6) ** (1/2) + 7) ** (1/2)
diff4 = PI - pi4    # diff = -3.989091382461396e-05
print(f"pi = {pi4}\ndiff = {diff4}")
pi5 = ((10 ** 100) / 11222.11122) ** (1/193)
diff5 = PI - pi5    # diff = -5.402922553798817e-11 # the most closest to the pi
print(f"pi = {pi5}\ndiff = {diff5}")


pi = 3.140845070422535
pi = 3.1415926534674368
pi = 6.283185460026612
pi = 3.1416325445036177
pi = 3.1415926536438223
