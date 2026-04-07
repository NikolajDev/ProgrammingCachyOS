'''Napíš funkciu 
spoj(zoznam,
 
retazec='')
, ktorá z daného zoznamu hodnôt (čísel alebo reťazcov) vyrobí jeden reťazec, ktorý obsahuje všetky prvky zoznamu, pričom medzi tieto hodnoty vloží zadaný 
retazec
 (podobne ako reťazcová metóda 
join()
). Napríklad:


>>> 
spoj
([
'12'
,
 
3
,
 
'456'
,
 
'7'
],
 
'+'
)


    '12+3+456+7'


>>> 
spoj
([
'12'
,
 
3
,
 
'456'
,
 
7
],
 
' <=> '
)


    '12 <=> 3 <=> 456 <=> 7'


>>> 
spoj
([],
 
'*'
)


    ''


>>> 
spoj
(
list
(
'python'
),
 
'*'
)


    'p*y*t*h*o*n'


>>> 
spoj
(
list
(
range
(
11
,
 
20
)))


    '111213141516171819'
'''