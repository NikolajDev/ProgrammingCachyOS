'''Napíš funkciu 
grange(start,
 
stop,
 
krok=1)
, ktorá bude generátorom (použije 
yield
) a bude generovať rovnakú postupnosť celých čísel ako štandardný 
range()
. Môžeš predpokladať, že parameter 
krok
 je väčší ako 
0
 (hoci výzvou by mohol byť aj záporný krok). Samozrejme, že vo funkcii nesmieš použiť funkciu 
range()
. Napríklad:


>>> 
tuple
(
grange
(
3
,
 
50
,
 
7
))


    (3, 10, 17, 24, 31, 38, 45)






Generátor by mal fungovať aj pre desatinné čísla:


>>> 
tuple
(
grange
(
1
,
 
5
,
 
0.5
))


    (1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5)
'''