'''Do funkcie 
max()
 z predchádzajúcej úlohy pridaj na koniec pomenovaný parameter 
key
 s náhradnou hodnotou 
None
. Teraz bude funkcia pracovať takto:




v prípade, že 
key
 má hodnotu 
None
, bude pracovať rovnako ako v predchádzajúcej úlohe


inak predpokladáme, že 
key
 je daná funkcia s jedným parametrom, vďaka tejto funkcii bude 
max
 hľadať taký prvok 
x
, pre ktorý je 
key(x)
 maximálny




Zapíš, napríklad:


def
 
max
(
*
post
,
 
key
=
None
):

    
...






alebo


def
 
max
(
prvy
,
 
*
post
,
 
key
=
None
):

    
...






Napríklad:


>>> 
max
(
3
,
 
7
,
 
11
,
 
4
)


    11


>>> 
max
(
3
,
 
7
,
 
11
,
 
4
,
 
key
=
lambda
 
x
:
 
-
x
)


    3


>>> 
max
([
3
,
 
7
,
 
11
,
 
4
],
 
key
=
str
)


    7






Nepoužívaj štandardnú funkciu 
max
 (aj štandardná funkcia 
max
 funguje presne takto s pomenovaným parametrom 
key
, môžeš to otestovať).
'''