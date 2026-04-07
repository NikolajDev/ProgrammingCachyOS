'''odovzdaj
 Napíš funkciu 
do_dvojrozmernej(postupnost,
 
sirka)
, ktorá bude v istom zmysle fungovať naopak ako funkcia 
do_radu
 z predchádzajúceho príkladu: funkcia dostáva postupnosť nejakých hodnôt (napríklad jednorozmerný zoznam) a vyrobí z nej dvojrozmernú tabuľku, v ktorej okrem posledného riadku majú všetky zadanú šírku. Posledný riadok môže byť kratší. Napríklad:


>>> 
t1
 
=
 
do_dvojrozmernej
(
range
(
10
),
 
3
)


>>> 
vypis
(
t1
)


       0    1    2


       3    4    5


       6    7    8


       9


>>> 
t2
 
=
 
do_dvojrozmernej
(
do_radu
(
t1
),
 
5
)


>>> 
vypis
(
t2
)


       0    1    2    3    4


       5    6    7    8    9


>>> 
vypis
(
do_dvojrozmernej
(
'programovanie'
,
 
5
))


     'p'  'r'  'o'  'g'  'r'


     'a'  'm'  'o'  'v'  'a'


     'n'  'i'  'e'
'''