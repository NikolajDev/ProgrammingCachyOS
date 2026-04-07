'''Naprogramuj tieto tri funkcie s parametrom typu 
Queue
 tak, aby sa nepoškodil obsah radu:




pocet_cisel(rad)
 zistí počet prvkov v rade, ktoré sú 
int
 alebo 
float


druhy(rad)
 vráti hodnotu druhého prvku radu (druhého pridaného prvku)


posledny(rad)
 vráti hodnotu posledného prvku radu (naposledy pridaného prvku)




Pre tieto funkcie to rieš najprv s pomocným radom (podobne, ako sme to riešili so zásobníkom) a potom aj bez pomocného radu pomocou zarážky (vyberané prvky sa ukladajú na koniec samotného radu). Otestuj:


>>> 
from
 
struktury
 
import
 
Queue


>>> 
q
 
=
 
Queue
([
'a'
,
 
27
/
10
,
 
'3'
,
 
37
])


>>> 
q


    Queue(('a', 2.7, '3', 37))


>>> 
pocet_cisel
(
q
)


    2


>>> 
druhy
(
q
)


    2.7


>>> 
posledny
(
q
)


    37


>>> 
q


    Queue(('a', 2.7, '3', 37))
'''