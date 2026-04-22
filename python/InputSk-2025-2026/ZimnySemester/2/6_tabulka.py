"""
Napíš funkciu tabulka(od=0, do=90, krok=10), ktorý vytvorá takúto tabuľku: pre všetky uhly (v stupňoch) zo zadaného intervalu a kroku vypíše druhé mocniny príslušných sínusov a kosínusov a aj ich súčet. Druhé mocniny vypíše na šírku 6 a 4 desatinné miesta, súčet bez udania šírky a počtu desatinných miest. Môžeš dostať takýto výstup:

>>> tabulka()
      0 sin**2=0.0000 cos**2=1.0000 súčet=1.0
     10 sin**2=0.0302 cos**2=0.9698 súčet=0.9999999999999999
     20 sin**2=0.1170 cos**2=0.8830 súčet=1.0
     30 sin**2=0.2500 cos**2=0.7500 súčet=1.0
     40 sin**2=0.4132 cos**2=0.5868 súčet=0.9999999999999999
     50 sin**2=0.5868 cos**2=0.4132 súčet=1.0
     60 sin**2=0.7500 cos**2=0.2500 súčet=1.0
     70 sin**2=0.8830 cos**2=0.1170 súčet=0.9999999999999999
     80 sin**2=0.9698 cos**2=0.0302 súčet=0.9999999999999999
     90 sin**2=1.0000 cos**2=0.0000 súčet=1.0
"""

from math import sin, cos, radians 

def tabulka(od: int=0, do: int=90, step:int=10):
    cos_help = 90
    for i in range(od, do+1, step):
        sinus = sin(radians(i))**2
        cosin = sin(radians(cos_help - i))**2
        semi_result = sinus + cosin
        print(f"""{i:7} sin**2={sinus**2:6.4f} cos**2={cosin**2:6.4f} sucet={semi_result}""")

tabulka()