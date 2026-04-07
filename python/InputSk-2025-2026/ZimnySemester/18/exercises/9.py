'''Napíš funkciu 
zisti(postupnost,
 
vzost=True)
, ktorá zistí (vráti 
True
 alebo 
False
), či je zadaná postupnosť hodnôt usporiadaná vzostupne. Vstupnú postupnosť 
neukladaj
 do žiadneho pomocného zoznamu. Parameter 
vzost
 s hodnotou 
False
 označuje, že kontroluješ, či je postupnosť usporiadaná zostupne. Vzostupné usporiadanie označuje, že pre žiadne dva susedné prvky postupnosti nie je prvý z nich väčší ako druhý. Malo by to fungovať, napríklad takto:


>>> 
zisti
([
1
,
 
3
,
 
3
,
 
4
])


True


>>> 
zisti
(
range
(
10
))


True


>>> 
zisti
(
range
(
10
),
 
False
)


False






Pri riešení tejto úlohy nepouži žiadne triedenie, ani štandardnú funkciu 
sorted
.
'''