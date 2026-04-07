'''Napíš funkciu 
sucet(post)
, ktorá vypočíta „súčet“ prvkov postupnosti 
post
. Predpokladaj, že všetky prvky sú rovnakého typu ako prvý prvok postupnosti. Ak je niektorý prvok iného typu ako prvý prvok, tak sa ho funkcia snaží najprv prekonvertovať na tento typ, ak sa ani to nedá, tak tento jeden prvok odignoruje. Napríklad:


>>> 
sucet
([
2
,
 
'3'
,
 
4.0
,
 
'päť'
])


    9


>>> 
sucet
([
'1'
,
 
2
,
 
0.3
,
 
'abc'
])


    '120.3abc'


>>> 
sucet
([[
1
,
2
],
 
3
,
 
'4x'
])


    [1, 2, '4', 'x']


>>> 
sucet
([(
1
,
 
2
),
 
(
3
,
 
4
),
 
[
5
]])


    (1, 2, 3, 4, 5)


>>> 
print
(
sucet
([]))
     
# pre prázdnu postupnosť


    None






Pomôcka: ak potrebuješ pretypovať 
b
 na rovnaký typ ako je 
a
, môžeš to urobiť takto: 
type(a)(b)
.
'''