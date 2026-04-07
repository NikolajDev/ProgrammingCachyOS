'''odovzdaj
 Napíš funkciu 
enum(postupnost)
, ktorá vráti (
return
) n-ticu dvojíc. V tejto n-tici je prvý prvok poradové číslo (od 
0
 do počet prvkov postupnosti mínus 1) a druhým je prvok z danej postupnosti. Malo by to dať rovnaký výsledok ako 
tuple(enumerate(postupnost))
 ale samozrejme, že bez použitia 
enumerate
. Napríklad:


>>> 
enum
([
12
,
 
'dva'
,
 
3.14
])


    ((0, 12), (1, 'dva'), (2, 3.14))






Úlohu môžeš riešiť buď bez pomoci generátorovej notácie alebo pomocou nej.
'''