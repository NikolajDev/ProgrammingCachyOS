'''Vylepši funkciu 
zlep(zoz)
 tak, aby fungovala správne aj pre obrázky v zozname, ktoré nie sú rovnako veľké. Funkcia si najprv vypočíta maximálnu šírku aj výšku, aby mohla jednotlivé obrázky rozložiť vo výslednom obrázku rovnomerne. Výsledný obrázok bude mať tie časti, ktoré nie sú pokryté obrázkom, priesvitné. Dávaj pozor na to, že príkaz 
obr.paste
 musíš zavolať inak pre obrázky s priesvitnosťou (
obr.mode
 
==
 
'RGBA'
) a v inom prípade.


Malo by korektne fungovať aj opätovné rozstrihanie takto zlepeného obrázka. Napríklad, pre rôzne veľké obrázky:


>>> 
obr1
 
=
 
...


>>> 
obr2
 
=
 
...


>>> 
obr3
 
=
 
...


>>> 
zoz
 
=
 
strihaj
(
zlep
([
obr1
,
 
obr2
,
 
obr3
]),
 
3
)






Zoznam 
zoz
 teraz obsahuje tri rovnako veľké obrázky, v ktorých sú pôvodné obrázky (
obr1
, 
obr2
 a 
obr3
) vycentrované.
'''