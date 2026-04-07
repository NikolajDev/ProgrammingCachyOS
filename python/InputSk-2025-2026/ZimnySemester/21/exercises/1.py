'''Naprogramujte interaktívny 
adventný kalendár
. Na pozadí sa zobrazí obrázok 
'mikulasaspol.jpg'
. Canvas bude mať rovnaké rozmery ako obrázok. Do mriežky 6x4 vygenerujte 24 okienok adventného kalendára. Na začiatku budú všetky obrázky kalendára zobrazené ako vločky (obrázok 
'0.gif'
) aj s príslušným číslom. Čísla (aj s príslušnými obrázkami) budú v mriežke rozmiestnené v náhodnom poradí. Napríklad:






Po kliknutí na ľubovoľné okienko kalendára sa vločka zmení na príslušný obrázok, a ak je to animovaný obrázok, bude sa animovať (striedať fázy animácie). Ak je to len jednofázový obrázok, prirob k nemu ďalších 7 fáz, ktoré vzniknú otáčaním prvej fázy postupne o uhly 
(10,
 
20,
 
10,
 
0,
 
-10,
 
-20,
 
-10)
. Napríklad:






Ak znovu klikneme na odkryté okienko kalendára, toto okienko sa zatvorí (zobrazí sa vločka aj s príslušným číslom).


Všetkým animáciám nastav náhodnú rýchlosť animovania od 100 do 500.


Všetky súbory k projektu si stiahneš z 
1cv21.zip


Tvoj projekt by mohol mať približne takúto štruktúru:


class
 
Karticka
:

    
canvas
 
=
 
None


    
def
 
__init__
(
self
,
 
x
,
 
y
,
 
meno_suboru
,
 
tik
=
100
):

        
...


    
def
 
dalsia_faza
(
self
):

        
...



class
 
Kalendar
:


    
def
 
__init__
(
self
):

        
...

        
self
.
canvas
.
bind
(
'<ButtonPress-1>'
,
 
self
.
otoc
)


    
def
 
otoc
(
self
,
 
event
):

        
...


    
def
 
timer
(
self
):

        
...



Kalendar
()
'''