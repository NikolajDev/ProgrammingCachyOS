'''Napíš funkciu 
max()
, ktorá môže mať ľubovoľný počet parametrov. Funkcia zistí maximálnu hodnotu. Ak je prázdny počet parametrov, funkcia vyvolá chybu, napríklad 
'TypeError:
 
chybajuci
 
parameter'
. Nepoužívaj štandardnú funkciu 
max
. Napríklad:


>>> 
max
(
9
,
 
13
,
 
11
)


    13


>>> 
max
(
*
'python'
)


    'y'


>>> 
max
()


    ...


    TypeError: chybajuci parameter






Do funkcie 
max()
 pridaj takéto správanie: v prípade, že má zadaný iba jeden parameter, predpokladáme, že je to iterovateľná štruktúra (napríklad 
list
, 
tuple
, 
set
, 
dict
, 
str
), vráti maximálnu hodnotu z tejto štruktúry. Inak bude pracovať tak, ako doteraz. Napríklad:


>>> 
max
((
3
,
 
'a'
),
 
(
3
,
 
'b'
),
 
(
2
,
 
'x'
))


    (3, 'b')


>>> 
max
(
9
,
 
13
,
 
11
)


    13


>>> 
p
 
=
 
(
9
,
 
13
,
 
11
)


>>> 
max
(
p
)


    13


>>> 
max
(
'python'
)


    'y'


>>> 
max
([])


    ...


    TypeError: chybajuci parameter






Môžeš otestovať, ako sa v týchto prípadoch správa štandardná funkcia 
max
.
'''