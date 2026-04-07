'''Napíš funkciu 
vyhod_riadok(meno_suboru,
 
index)
, ktorá z textového súboru odstráni zadaný riadok (
index
 je číslo riadka pri číslovaní od 
0
). Ak sa 
index
 rovná 
-1
, funkcia vyhodí posledný riadok. Ak riadok so zadaným indexom neexistuje, funkcia nerobí nič. Napríklad, pre súbor:


Od učenia ešte
nikto nezomrel,
  ale načo riskovať.

Albert Einstein





volanie:


>>> 
vyhod_riadok
(
'text1.txt'
,
 
1
)






odstráni riadok s indexom 1, teda druhý v poradí; v súbore teraz budú tieto riadky:


Od učenia ešte
  ale načo riskovať.

Albert Einstein
'''