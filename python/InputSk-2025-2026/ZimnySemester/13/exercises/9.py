'''Zadefinuj novú triedu 
Korytnacka
, ktorá bude odvodená od triedy 
Pero
 z úlohy (8):




metóda 
__init__()
 vytvorí pero v strede plochy a do nového atribútu 
uhol
 nastaví 0 (teda otočenie smerom na východ)


metódy 
lt(uhol)
 a 
rt(uhol)
 zmenšia, resp. zväčšia atribút 
uhol
 o zadanú hodnotu, uhly sa budú počítať v stupňoch


metóda 
fd(dlzka)
 presunie pero (zavolá metódu 
setpos()
) o zadanú dĺžku, ktorá je v momentálnom smere natočenia




asi použiješ približne takýto vzorec pre nové 
x
 a 
y
: 
x+dlzka*cos(uhol)
, 
y+dlzka*sin(uhol)


nezabudni, že 
sin()
 a 
cos()
 fungujú v radiánoch, pričom atribút 
uhol
 pracuje v stupňoch






nepouží modul 
turtle




Otestuj napríklad takto:


class
 
Korytnacka
(
Pero
):

    
def
 
__init__
(
self
):

        
...


    
def
 
lt
(
self
,
 
uhol
):

        
...


    
def
 
rt
(
self
,
 
uhol
):

        
...


    
def
 
fd
(
self
,
 
dlzka
):

        
...



#---- test -------



t
 
=
 
Korytnacka
()


for
 
i
 
in
 
range
(
1
,
 
200
,
 
2
):

    
t
.
fd
(
i
)

    
t
.
lt
(
89
)
'''