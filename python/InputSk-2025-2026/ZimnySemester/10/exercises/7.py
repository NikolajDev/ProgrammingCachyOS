'''Textový súbor v každom riadku obsahuje niekoľko slov, oddelených medzerou (riadok môže byť aj prázdny). Napíš funkciu 
citaj(meno_suboru)
, ktorá prečíta tento súbor a vyrobí z neho dvojrozmernú tabuľku slov: každý riadok tabuľky zodpovedá jednému riadku súboru. Napríklad, ak súbor 
'text.txt'
 obsahuje:


Anička dušička
kde si bola
keď si si čižmičky
zarosila





potom


>>> 
x
 
=
 
citaj
(
'text.txt'
)


>>> 
x


    [['Anička', 'dušička'], ['kde', 'si', 'bola'], ['keď', 'si', 'si', 'čižmičky'], ['zarosila']]


>>> 
vypis
(
x
)


      'Anička'  'dušička'


         'kde'       'si'     'bola'


         'keď'       'si'       'si' 'čižmičky'


    'zarosila'
'''