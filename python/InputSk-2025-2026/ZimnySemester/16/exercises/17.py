'''Zapíš dve verzie funkcie 
spoj(gen1,
 
gen2)
, ktorá vygeneruje (vráti ako generátor) najprv všetky prvky 
gen1
 potom všetky prvky 
gen2




vyskúšaj nielen s parametrami typu generátor, ale napríklad aj so zoznamami a reťazcami


na riešenie môžeš použiť (ale nemusíš) funkcie 
iter
 a 
next
 a zrejme aj príkaz 
yield


zapíš verziu funkcie 
spoj(*gen)
, v ktorej sa spája ľubovoľne veľa generátorov




Napríklad:


>>> 
g
 
=
 
spoj
(
iter
(
range
(
5
)),
 
iter
(
range
(
10
,
 
0
,
 
-
2
)))


>>> 
g


    <generator object spoj at 0x00A823C0>


>>> 
print
(
*
g
)


    0 1 2 3 4 10 8 6 4 2


>>> 
g
 
=
 
spoj
(
iter
(
range
(
5
)),
 
iter
(
'ahoj'
),
 
iter
(
range
(
10
,
 
0
,
 
-
2
)))


>>> 
print
(
*
g
)


    0 1 2 3 4 a h o j 10 8 6 4 2
'''