'''-
 Napíš funkciu 
kruznica(r)
, ktorá nakreslí kružnicu s polomerom 
r
 a so stredom, ktorý je v momentálnej pozícii korytnačky. Kružnicu kresli ako pravidelný 36-uholník. Uvedom si, že ak by strana tohto 36-uholníka bola 
d
, tak obvod vypočítame ako 
2*pi*r
 
=
 
36*d
. Z tohto vzťahu vieš vypočítať 
d
 a teda nakresliť pravidelný 36-uholník. Po skončení kreslenia, korytnačka bude v rovnakej pozícii ako začala. Nepoužívaj metódu 
setpos
. Vyskúšaj:


t
.
dot
(
200
,
 
'yellow'
)


kruznica
(
100
)


t
.
pu
()


t
.
fd
(
120
)


t
.
lt
(
90
)


t
.
fd
(
100
)


t
.
rt
(
37
)


t
.
pd
()


t
.
dot
(
140
,
 
'gold'
)


kruznica
(
70
)






dostaneš (dva žlté kruhy kreslené pomocou 
dot
 sú tu len na kontrolu):
'''