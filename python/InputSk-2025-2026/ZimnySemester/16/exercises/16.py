'''Zapíš funkciu 
zdvoj(gen)
, ktorá vygeneruje každý prvok 2-krát za sebou - funkcia vráti generátor




vyskúšaj nielen s parametrom typu generátor, ale napríklad aj so zoznamom alebo s reťazcom


na riešenie môžeš použiť (ale nemusíš) funkcie 
iter
 a 
next
 a zrejme aj príkaz 
yield




Napríklad:


>>> 
g
 
=
 
zdvoj
(
i
**
2
 
for
 
i
 
in
 
range
(
1
,
 
5
))


>>> 
g


    <generator object zdvoj at 0x022A6828>


>>> 
list
(
g
)


    [1, 1, 4, 4, 9, 9, 16, 16]


>>> 
zdvoj
(
'Python'
)


    ...


>>> 
zdvoj
([
2
,
 
3
,
 
5
])


    ...
'''