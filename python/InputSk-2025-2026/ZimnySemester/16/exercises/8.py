'''Napíš funkciu 
map2(fun,
 
param1,
 
param2)
, ktorá bude pracovať podobne ako funkcia 
mapuj()
 z prednášky, len funkcia 
fun
 očakáva dva parametre: jeden z postupnosti 
param1
 a druhý z postupnosti 
param2
. Ak majú tieto postupnosti rôznu dĺžku, tak berie len počet kratšej z nich. Nepouži štandardnú funkciu 
map
. Napríklad:


>>> 
def
 
f
(
x
,
 
y
):
 
return
 
x
 
*
 
y


>>> 
map2
(
f
,
 
'python'
,
 
range
(
1
,
 
6
))


    ['p', 'yy', 'ttt', 'hhhh', 'ooooo']


>>> 
map2
(
f
,
 
(
'a'
,
 
4
,
 
(
1
,
 
2
)),
 
[
3
,
 
5
,
 
2
])


    ['aaa', 20, (1, 2, 1, 2)]






Otestuj, či takto funguje aj štandardná funkcia 
map
 (keď má tri parametre, tak prvým je binárna funkcia, ktorá sa aplikuje na prvky dvoch postupností).
'''