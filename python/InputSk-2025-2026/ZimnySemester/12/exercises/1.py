'''odovzdaj
 Zapíš definíciu triedy 
Zlomok
, ktorá v 
inicializácii
 vytvorí dva atribúty 
citatel
 a 
menovatel
. 
Metóda
 
vypis()
 vypíše pomocou 
print()
 tento zlomok v tvare 
zlomok
 
je
 
3/8
. Napríklad test:


z1
 
=
 
Zlomok
(
3
,
 
8
)


z2
 
=
 
Zlomok
(
2
,
 
4
)


z1
.
vypis
()


z2
.
vypis
()






vypíše


zlomok
 
je
 
3
/
8


zlomok
 
je
 
2
/
4






Do triedy 
Zlomok
 pridaj tieto dve metódy:




metóda
 
__str__()
 vráti (nič nevypisuje) reťazec v tvare 
3/8


metóda
 
float()
 vráti (nič nevypisuje) desatinné číslo, ktoré reprezentuje daný zlomok; výsledok zaokrúhli na 2 desatinné miesta




Napríklad test:


z
 
=
 
Zlomok
(
3
,
 
8
)


print
(
'z je'
,
 
z
)
     
# print tu zavolá __str__


print
(
'z je'
,
 
z
.
float
())


w
 
=
 
Zlomok
(
2
,
 
4
)


print
(
'w je'
,
 
w
)


print
(
'w je'
,
 
w
.
float
())






vypíše


z
 
je
 
3
/
8


z
 
je
 
0.38


w
 
je
 
2
/
4


w
 
je
 
0.5
'''