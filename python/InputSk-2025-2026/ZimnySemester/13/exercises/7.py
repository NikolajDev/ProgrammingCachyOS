'''Zadefinuj triedu 
UcetHeslo
, ktorá je 
odvodená
 z triedy 
Ucet
 a má takto zmenené správanie:




__init__(meno,
 
heslo,
 
suma)
 - k účtu si zapamätá aj heslo


vklad(suma)
 - si najprv vypýta heslo a až keď je správne, zrealizuje vklad


vyber(suma)
 - si najprv vypýta heslo a až keď je správne, zrealizuje výber, inak vráti 
None


pri definovaní týchto metód využite volania ich pôvodných verzií z triedy 
Ucet




Otestujte napríklad:


mbank
 
=
 
UcetHeslo
(
'mbank'
,
 
'gigi'
)


csob
 
=
 
Ucet
(
'csob'
,
 
100
)


tatra
 
=
 
UcetHeslo
(
'tatra'
,
 
'gogo'
,
 
17
)


sporo
 
=
 
Ucet
(
'sporo'
,
 
50
)


mbank
.
vklad
(
sporo
.
vyber
(
30
)
 
+
 
tatra
.
vyber
(
30
))


csob
.
vyber
(
-
5
)


spolu
 
=
 
0


for
 
ucet
 
in
 
mbank
,
 
csob
,
 
tatra
,
 
sporo
:

    
print
(
ucet
)

    
spolu
 
+=
 
ucet
.
stav
()


print
(
'spolu = '
,
 
spolu
)






Tento program si najprv dvakrát vypýta heslo:


zadaj
 
heslo
 
uctu
 
tatra
:
 
gogo


zadaj
 
heslo
 
uctu
 
mbank
:
 
gigi








a až potom (po správnom zadaní hesiel) vypíše to isté, ako predtým


zisti, čo sa stane s účtami, keď pre 
'mbank'
 určíme chybné heslo
'''