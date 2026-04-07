'''Triedu 
Cas
 z prednášky doplň tak, aby operácie sčitovania a odčitovania fungovali nielen s celými číslami (pripočítava, resp. odpočítava sekundy), ale aj s n-ticami (prvým prvkom sú hodiny, druhým minúty a tretím sekundy). Napríklad:


>>> 
c
 
=
 
Cas
(
8
,
 
10
,
 
34
)


>>> 
c


    8:10:34


>>> 
c
 
+
 
640


    8:21:14


>>> 
(
1
,
 
55
)
 
+
 
c


    10:05:34


>>> 
c
 
-
 
100


    8:08:54






Pomocou modulu 
time
 a funkcie vieme zistiť momentálny čas v počítači. Napríklad:


>>> 
import
 
time


>>> 
time
.
localtime
()


    time.struct_time(tm_year=2017, tm_mon=11, tm_mday=22, tm_hour=8, tm_min=26, tm_sec=12,


    tm_wday=1, tm_yday=327, tm_isdst=0)


>>> 
time
.
localtime
()[
3
:
6
]


    (8, 26, 24)






Napíš ešte globálnu funkciu 
teraz()
, ktorá vráti inštanciu triedy 
Cas
 s momentálnym časom. Napríklad:


>>> 
c
 
=
 
teraz
()


>>> 
type
(
c
)


    <class '__main__.Cas'>


>>> 
c


    8:34:07


>>> 
teraz
()


    8:35:22
'''