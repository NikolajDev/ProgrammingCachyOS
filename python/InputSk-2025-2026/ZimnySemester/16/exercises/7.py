'''Napíš funkciu 
aplikuj(...)
, ktorej parametrami sú nejaké funkcie, okrem posledného parametra, ktorým je nejaká hodnota. Funkcia postupne zavolá všetky tieto funkcie s danou hodnotou, pričom každú ďalšiu funkciu aplikuje na predchádzajúci výsledok. Napríklad 
aplikuj(f1,
 
f2,
 
f3,
 
x)
 vypočíta 
f3(f2(f1(x)))
. Funkcia by mala správne pracovať pre ľubovoľný nenulový počet parametrov. Napríklad:


>>> 
aplikuj
(
float
,
 
int
,
 
str
,
 
'-314159e-3'
)


    '-314'


>>> 
def
 
rev
(
x
):
 
return
 
x
[::
-
1
]


>>> 
aplikuj
(
str
,
 
rev
,
 
int
,
 
1074
)


    4701


>>> 
aplikuj
(
abs
,
 
lambda
 
x
:
 
x
+
7
,
 
-
17
)


    24
'''