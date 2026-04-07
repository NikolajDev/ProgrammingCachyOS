'''Najprv nakresli kruh so stredom (
x0
, 
y0
) a polomerom 
r
 (napríklad pre 
r,
 
x0,
 
y0
 
=
 
120,
 
150,
 
130
). Potom každé kliknutie do vnútra kruhu zmení farbu výplne na odtieň šedej - čím bližšie do stredu tým tmavšie (v strede kruhu čierne), ku okraju svetlejšie (na obvode biele). Zrejme pri kliknutí vypočítaš vzdialenosť od stredu kruhu a toto číslo potom prepočítaš na celé číslo od 
0
 do 
255
 (napríklad 
f
 
=
 
int(255
 
*
 
vzd
 
/
 
r)
). Z tohto čísla vyrobíš šedý odtieň pre farbu kruhu (zrejme 
rgb(f,
 
f,
 
f)
). Nepoužívaj 
global
. Popri klikaniu zabezpeč, aby fungovalo aj ťahanie myšou.
'''