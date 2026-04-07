'''Atribúty 
meno
, 
typ
 a 
zvuk
 prerob na 
property
:




najprv ich všetky premenuj tak, aby začínali znakom podčiarkovník


v triede 
Zviera
 pre všetky z nich zadefinuj zodpovedajúci 
getter
 v tvare 
daj_atribút


atribúty 
meno
 a 
zvuk
 budú mať aj svoj 
setter
:




metóda 
zmen_meno
 nastaví prvé písmeno mena na veľké a ostatné na malé


metóda 
zmen_zvuk
 najprv zistí, či nový zvuk obsahuje znak 
'-'
 a ak nie, tak zvuk zreťazí za seba a vloží znak 
'-'
,








Napríklad:


>>> 
z3
.
zmen_zvuk
(
'vrr'
)


>>> 
z3
.
daj_zvuk
()


    'vrr-vrr'


>>> 
z4
.
zmen_zvuk
(
'GA-GA'
)


>>> 
z4
.
daj_zvuk
()


    'GA-GA'








vyrob 
meno
, 
typ
 a 
zvuk
 ako 
property
, pričom 
typ
 nebude mať definovaný 
setter
 (zapíšeš 
typ
 
=
 
property(daj_typ)
)




Otestuj, napríklad:


>>> 
z3
.
zvuk
 
=
 
'vrr'


>>> 
z4
.
meno
 
=
 
'grETA'


>>> 
z2
.
typ
 
=
 
'cat'
'''