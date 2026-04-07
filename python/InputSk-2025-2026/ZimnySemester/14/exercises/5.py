'''-
 Napíš funkciu 
cele(hodnota)
, ktorá pomocou 
int
 prevedie danú hodnotu na celé číslo. Ak sa to nedá, funkcia vráti 
0
. Použi 
try-except
, v ktorom uvedieš dva rôzne typy chýb. Malo by fungovať, napríklad:


>>> 
cele
(
12.3
)


    12


>>> 
cele
(
'13'
)


    13


>>> 
cele
([])


    0


>>> 
cele
(
'12.3'
)


    0
'''