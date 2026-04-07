'''Do grafickej plochy nakresli kružnicu (napríklad pre 
r,
 
x0,
 
y0
 
=
 
100,
 
150,
 
120
). Potom naprogramuj časovač, ktorý bude rovnomerne posúvať červenú bodku (kruh s polomerom 5) na obvode tejto kružnice (po každom tiknutí časovača posunie jeho pozíciu na kružnici o uhol 
10
 stupňov). Posúvanie kruhu budeš robiť pomocou 
canvas.coords()
.


Teraz do aplikácie pridaj nový posúvač 
Scale
, pomocou ktorého sa bude dať riadiť rýchlosť tikania časovača, napríklad takto:


cas
 
=
 
tkinter
.
Scale
(
orient
=
'horizontal'
,
 
from_
=
50
,
 
to
=
1000
,
 
resolution
=
50
)


cas
.
pack
()






Zrejme samotná funkcia časovača nastaví svoj čas v 
after()
 pomocou 
cas.get()
.
'''