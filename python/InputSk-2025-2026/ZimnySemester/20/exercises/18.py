'''Napíš funkciu 
otacaj(obr,
 
n)
, ktorá vytvorí 
n
-prvkový zoznam obrázkov. Každý vznikne otočením pôvodného obrázka o nejaký uhol tak, že tieto otáčania budú rovnomerne všetkými smermi (napríklad pre 
n=5
 budú tieto uhly 
0
, 
72
, 
144
, …). Dbaj na to, aby sa pri otáčaní nestratili žiadne časti obrázka (
expand=True
) a oblasti, ktoré otáčaním pribudnú boli priesvitné. Výsledný zoznam vráti ako výsledok funkcie. Otestuj:


>>> 
zlep2
(
otacaj
(
Image
.
open
(
'pyton.png'
),
 
6
))
.
show
()


>>> 
zlep2
(
otacaj
(
Image
.
open
(
'tiger.bmp'
),
 
3
))
.
show
()


>>> 
zlep2
(
otacaj
(
Image
.
open
(
'vtak.gif'
),
 
15
))
.
show
()
'''