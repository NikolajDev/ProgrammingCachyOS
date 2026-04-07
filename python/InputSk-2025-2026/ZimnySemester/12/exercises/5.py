'''-
 Zadefinuj triedu 
Okno
, ktorá otvorí grafické okno so zadaným textom. 
Inicializácia
 (metóda 
__init__(text)
) vytvorí nový 
canvas
 (výšky 100) a do jeho stredu vypíše zadaný text fontom veľkosti 50. V svojich atribútoch si zapamätá 
canvas
 aj identifikačný kód pre 
create_text()
. Ďalšie dve metódy menia vypísaný text:




metóda
 
zmen(text)
 zmení vypísaný text (zrejme na to použije 
itemconfig()
)


metóda
 
farba(farba)
 zmení farbu vypísaného textu (zrejme na to použije 
itemconfig()
)




Napríklad:


import
 
tkinter


okno
 
=
 
Okno
(
'ahoj'
)


okno
.
farba
(
'red'
)


okno
.
zmen
(
'Python'
)


okno
 
=
 
Okno
(
'hello'
)


okno
.
farba
(
'green'
)
'''