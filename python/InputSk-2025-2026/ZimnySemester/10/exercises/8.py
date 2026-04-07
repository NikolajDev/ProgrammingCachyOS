'''Funkcia 
zapis(tab,
 
meno_suboru)
 je opačná k funkcii 
citaj
 v predchádzajúcej úlohe: zapíše danú dvojrozmernú tabuľku slov do súboru. Napríklad:


>>> 
x
 
=
 
[[
'Anička'
,
 
'dušička'
],
 
[
'kde'
,
 
'si'
,
 
'bola'
],
 
[
'keď'
,
 
'si'
,
 
'si'
,
 
'čižmičky'
],
 
[
'zarosila'
]]


>>> 
zapis
(
x
,
 
'text1.txt'
)






vytvorí rovnaký súbor ako bol 
'text.txt'
.


Uvedom si, že ak by vstupná dvojrozmerná tabuľka obsahovala čísla, táto funkcia vytvorí korektný súbor čísel, napríklad:


>>> 
zapis
([[
1
,
 
11
,
 
21
],
 
[
345
],
 
[
-
5
,
 
10
]],
 
'cisla.txt'
)






vytvorí súbor 
'cisla.txt'
:


1
 
11
 
21


345


-
5
 
10
'''