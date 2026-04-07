'''Napíš funkciu 
stvorce(retazec,
 
vel=60)
, ktorá dostáva dva parametre: veľkosť štvorca a znakový reťazec s menami farieb. Funkcia nakreslí rad farebných štvorcov veľkosti 
vel
, ktoré budú zafarbené farbami z reťazca. Zrejme štvorcov bude toľko, koľko farieb je v reťazci. Pre takéto volanie:


stvorce
(
'red blue purple red gold'
,
 
40
)






by si mohol dostať takýto obrázok:






Teraz túto funkciu zovšeobecni takto: parameter 
retazec
 môže pred každým menom farby obsahovať celé číslo, ktoré označuje veľkosť príslušného štvorca. Funkcia bude tieto štvorce kresliť vedľa seba, bude túto postupnosť štvorcov opakovať, ale len dovtedy, kým by nasledovný nevypadol z grafickej plochy (tento reťazec sa stále opakuje od začiatku). Do premennej 
sirka
 nastav nejakú šírku grafickej plochy a zavolaj funkciu, napríklad takto:


sirka
 
=
 
450


canvas
 
=
 
tkinter
.
Canvas
(
width
=
sirka
)


canvas
.
pack
()



stvorce
(
'40 red 20 blue purple 40 red 30 gold'
)






Mohol by si dostať takýto obrázok:






Všimni si, že fialový (
'purple'
) štvorec nemá určenú svoju veľkosť, teda sa použije náhradná veľkosť 
60
.
'''