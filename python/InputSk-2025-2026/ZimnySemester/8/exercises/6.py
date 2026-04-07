'''Napíš funkciu 
spirala(d,
 
krok,
 
uhol)
, ktorá nakreslí takúto špirálu: prvá úsečka je dĺžky 
d
, každá ďalšia je o 
krok
 dlhšia, pritom sa korytnačka otáča o zadaný 
uhol
. Takáto špirála sa bude skladať z maximálne 
200
 úsečiek, ale prestane sa kresliť vtedy, keď sa vzdiali od počiatku o viac ako 
250
. Aby sa kreslila čo najrýchlešie, bude treba okrem 
turtle.delay(0)
 nastaviť aj 
t.speed(0)
 a tiež skryť tvar korytnačky pomocou 
t.ht()
.


Teraz pridaj posúvač:


tkinter
.
Scale
(
command
=
rob
,
 
orient
=
'horizontal'
,
 
from_
=
5
,
 
to
=
179
,
 
length
=
300
)
.
pack
()






Takto vytvorený posúvač pri každej zmene bežca vyvolá funkciu 
rob
 - táto musí mať jeden parameter, v ktorom príde informácia o momentálnej hodnote posúvača, lenže ako reťazec. Funkcia by mala zabezpečiť prekreslenie špirály podľa nového uhla - najlepšie inicializovaním pomocou 
t.reset()
 (ten ale resetuje aj jej 
speed
 a viditeľnosť 
ht
).
'''