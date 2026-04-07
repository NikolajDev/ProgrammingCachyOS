'''Napíš funkciu 
zapis(zoz,
 
meno,
 
pripona)
, ktorá v parametri 
zoz
 dostáva postupnosť obrázkov a všetky tieto obrázky uloží do súborov s menami ‚meno0.pripona‘, ‚meno1.pripona‘, ‚meno2.pripona‘, … Otestuj napríklad:


>>> 
zapis
(
strihaj_gif
(
Image
.
open
(
'vtak.gif'
)),
 
'temp/vtak'
,
 
'png'
)






V priečinku 
temp
 by malo vzniknúť 8 obrázkových súborov s menami 
vtak0.png
, 
vtak1.png
, 
vtak2.png
, … Môžeš predpokladať, že priečinok 
temp
 už existoval predtým. Ak by si chcel takýto priečinok vytvárať vo funkcii, môžeš použiť:


import
 
os


os
.
makedirs
(
'temp'
,
 
exist_ok
=
True
)
'''