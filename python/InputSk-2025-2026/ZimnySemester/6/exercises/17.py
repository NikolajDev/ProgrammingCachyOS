'''Napíš funkciu 
kresli(meno_suboru)
, ktorá vykreslí krivku zadefinovanú v zadanom textovom súbore. V každom riadku súboru sú dve celé čísla súradnice bodov 
x
, 
y
. Napríklad pre súbor:


100
 
100


150
 
200


200
 
150


150
 
150






by mal nakresliť takúto krivku (v každom vrchole je malý krúžok):






Ak sa vo vstupnom súbore nachádza prázdny riadok, tento označuje, že za ním nasleduje ďalšia skupina bodov, ktorá ale nie je s predchádzajúcimi bodmi spojená. Napríklad:


100
 
100


150
 
200


200
 
150


150
 
150



220
 
50


320
 
50


320
 
150


220
 
150


220
 
50



50
 
30


150
 
70


80
 
90


50
 
30






nakreslí:
'''