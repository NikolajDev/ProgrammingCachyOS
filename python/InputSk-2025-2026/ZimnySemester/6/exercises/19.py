'''Napíš funkciu 
body_na_kruznici(meno_suboru,
 
n,
 
r,
 
x,
 
y)
, ktorá vygeneruje súbor s daným menom. Tento bude obsahovať 
n+1
 riadkov, pričom v každom budú súradnice nejakého bodu ako dvojica 
celých čísel
 oddelená medzerou. Súbor bude obsahovať body pravidelného 
n
-uholníka, ktoré sú rozložené na kružnici s polomerom 
r
 a so stredom v 
(x,
 
y)
. Zrejme prvý a posledný (
n+1
) bod budú rovnaké, aby sa pri kreslení tento 
n
-uholník uzavrel. Takto vytvorený súbor by sa mohol využiť vo funkcii 
kresli
 z (5) úlohy, napríklad:


>>> 
body_na_kruznici
(
'body4.txt'
,
 
20
,
 
120
,
 
250
,
 
130
)


>>> 
kresli
(
'body4.txt'
)






nakreslí takýto 20-uholník:






to isté pre trojuholník:
'''