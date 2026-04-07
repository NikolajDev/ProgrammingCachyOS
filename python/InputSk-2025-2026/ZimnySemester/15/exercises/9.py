'''Napíš funkcie 
push_dno(stack,
 
hodnota)
, 
inc(stack)
 a 
nechaj_parne(stack)
. Pri všetkých využiješ pomocný zásobník. Funkcia 
push_dno(stack,
 
hodnota)
 vloží na dno zásobníka danú hodnotu, napríklad:


>>> 
z
 
=
 
Stack
((
3
,
 
5
,
 
7
,
 
11
))


>>> 
push_dno
(
z
,
 
'z'
)


>>> 
z


    Stack(('z', 3, 5, 7, 11))






Funkcia 
inc(stack)
 ku všetkým hodnotám v zásobníku pripočíta (ak sa dá) 
1
, napríklad:


>>> 
cisla
 
=
 
Stack
([
1
,
 
2
,
 
4
,
 
6
,
 
10
])


>>> 
cisla
.
push
(
'a'
)


>>> 
inc
(
cisla
)


>>> 
cisla


    Stack((2, 3, 5, 7, 11, 'a'))






Funkcia 
nechaj_parne(stack)
 ponechá v zásobníku len celé čísla, ktoré sú ešte aj párne, napríklad:


>>> 
st
 
=
 
Stack
(
range
(
3
,
 
10
))


>>> 
st
.
push
(
'x'
)


>>> 
st


    Stack((3, 4, 5, 6, 7, 8, 9, 'x'))


>>> 
nechaj_parne
(
st
)


>>> 
st


    Stack((4, 6, 8))
'''