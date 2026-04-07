'''Pre dva obrázkové súbory 
'pismena.png'
 a 
'cislice.png'
 napíš funkcie:




velky_text(text)
 - vytvorí jeden obrázok z písmen v danom texte (iné znaky ignoruje), t.j. text rozoberie na písmená a výsledný obrázok poskladá zo zodpovedajúcich obrázkov v rozstrihanom súbore 
'pismena.png'
;


velke_cislo(cislo)
 - podobná ako 
velky_text
 - dané číslo rozloží na cifry a poskladá z nich jeden obrázok zlepením obrázkov cifier zo súboru 
'cislice.png'




Zrejme v oboch prípadoch využiješ funkcie 
strihaj
 a 
zlep
. Otestuj:


>>> 
velky_text
(
'Python'
)
.
show
()


>>> 
velke_cislo
(
2
**
100
)
.
show
()
'''