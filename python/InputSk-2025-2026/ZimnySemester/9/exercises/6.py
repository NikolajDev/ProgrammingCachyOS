'''odovzdaj
 Napíš funkciu 
sucet(zoznam)
, ktorá bez cyklov, ale pomocou rekurzie zistí súčet prvkov zoznamu, resp. ľubovoľnej postupnosti celých čísel. Prvkami sú len celé čísla. Otestuj, napríklad:


>>> 
sucet
([
2
,
 
4
,
 
6
,
 
8
])


    20


>>> 
sucet
(())


    0


>>> 
sucet
(
range
(
500
))


    124750






Rekurzia bude fungovať na takomto princípe:




triviálny prípad: zoznam je prázdny


inak: rekurzívne vypočítaj súčet všetkých prvkov zoznamu okrem prvého a k výsledku pripočítaj prvý prvok:




def
 
sucet
(
zoznam
):

    
if
 
len
(
zoznam
)
 
==
 
0
:

        
return
 
0

    
return
 
zoznam
[
0
]
 
+
 
sucet
(
zoznam
[
1
:])






Ak otestujeme 
sucet(range(2000))
, spadne to na pretečení rekurzie. Napíš novú verziu tejto rekurzívnej funkcie tak, tak aby fungovalo aj 
sucet(range(10000))
. Inšpiruj sa riešením funkcie 
otoc
 z prednášky:




triviálny prípad: zoznam je prázdny alebo jednoprvkový


inak: zoznam sa rozdelí na dve polovice a rekurzívne sa zistí súčet pre každú polovicu zvlášť
'''