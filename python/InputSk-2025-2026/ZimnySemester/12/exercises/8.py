'''-
 Zadefinuj triedu 
Klikanie
 s dvomi metódami 
__init__
 a 
klik
:




metóda 
__init__
 (okrem 
self
 nemá ďalšie parametre) vytvorí grafickú plochu (do 
self.canvas
) a zviaže ju (
bind
) s metódou 
self.klik
 pri kliknutí do plochy (
'<ButtonPress>'
)


metóda 
klik
 zrejme musí mať jeden parameter 
event
 (okrem 
self
), z ktorého získa 
x
 a 
y
 kliknutého miesta; metóda na toto kliknuté miesto nakreslí kružnicu s polomerom 
5




Teraz do triedy 
Klikanie
 pridaj ďalšiu metódu:




metóda 
vypis
 vypíše momentálny zoznam všetkých kliknutých bodov (dvojíc čísel), napríklad v tvare:




>>> 
k
.
vypis
()
          
# zavolané po troch kliknutých bodoch


    (162, 129)


    (231, 51)


    (273, 199)






Metódu 
klik
 uprav tak, aby okrem kreslenia malej kružnice spojila úsečkou naposledy nakreslený bod s predchádzajúcim bodom (zrejme okrem prvého kliknutia). Nepoužívaj globálne premenné.
'''