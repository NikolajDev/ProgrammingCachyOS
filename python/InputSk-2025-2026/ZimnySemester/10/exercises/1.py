'''-
 Modifikuj funkciu 
vypis(tab,
 
sirka=4)
, ktorá vypisuje dvojrozmernú tabuľku do riadkov, pričom každý prvok je formátovaný na zadanú šírku, napríklad pre 
sirka=5
 takto 
f'{repr(prvok):>5}'
 (alebo 
f'{repr(prvok):>{sirka}}'
). Otestuj:


>>> 
vypis
([[
1
,
 
6
,
 
3.14
],
 
[
0.5
,
 
1.5
,
 
2.5
]],
 
5
)


        1     6  3.14


      0.5   1.5   2.5


>>> 
vypis
([[
1
,
 
2
,
 
3
],
 
[
None
,
 
None
],
 
[
'4'
,
 
'5'
,
 
'6'
],
 
[
'Python'
,
 
3.9
]])


       1    2    3


    None None


     '4'  '5'  '6'


    'Python'  3.9






Funkciu teraz vylepši takto: 
vypis(tab,
 
sirka=None)
, kde parameter 
sirka
 s hodnotou 
None
 znamená, že sa najprv zistí šírka „najširšieho“ prvku v tabuľke (teda pomocou 
len(repr(prvok))
) a táto hodnota sa nastaví ako šírka výpisu. Pre nastavenú číselnú hodnotu šírky sa to bude správať rovnako ako v predchádzajúca verzia. Napríklad:


>>> 
vypis
([[
1
,
 
2
],
 
[
3
,
 
4
,
 
5
,
 
6
],
 
[
7
,
 
8
,
 
9
]])


    1 2


    3 4 5 6


    7 8 9


>>> 
vypis
([[
1
,
 
2
],
 
[
3
,
 
4
,
 
555
,
 
6
],
 
[
7
,
 
8
,
 
9
]])


      1   2


      3   4 555   6


      7   8   9


>>> 
vypis
([[
1
,
 
2
],
 
[
3
,
 
'4'
,
 
5
,
 
6
],
 
[
7
,
 
8
,
 
-
9
]],
 
1
)


    1 2


    3 '4' 5 6


    7 8 -9


>>> 
vypis
([[
1
,
 
2
,
 
3
],
 
[
None
,
 
None
],
 
[
'4'
,
 
'5'
,
 
'6'
],
 
[
'Python'
,
 
3.9
]])


           1        2        3


        None     None


         '4'      '5'      '6'


    'Python'      3.9






Pri riešení tejto úlohy skús čo najviac využiť generátorovú notáciu.
'''