'''Zadefinuj triedu 
Ucet
 s týmito metódami:




__init__(meno,
 
suma)
 - meno účtu a počiatočná suma, napríklad 
Ucet('mbank',
 
100)
 alebo 
Ucet('jbanka')


__str__()
 - reťazec v tvare 
'ucet
 
mbank
 
->
 
100
 
euro'
 alebo 
ucet
 
jbanka
 
->
 
0
 
euro


stav()
 - vráti momentálny stav účtu (vráti sumu na účte)


vklad(suma)
 - danú sumu pripočíta k účtu


vyber(suma)
 - vyberie sumu z účtu (len ak je to kladné číslo), ak je na účte menej ako požadovaná suma, vyberie len toľko koľko sa dá, metóda vráti (
return
) vybranú sumu




Otestuj, napríklad takto:


mbank
 
=
 
Ucet
(
'mbank'
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
 
Ucet
(
'tatra'
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






vypíše:


ucet
 
mbank
 
->
 
47
 
euro


ucet
 
csob
 
->
 
100
 
euro


ucet
 
tatra
 
->
 
0
 
euro


ucet
 
sporo
 
->
 
20
 
euro


spolu
 
=
  
167
'''