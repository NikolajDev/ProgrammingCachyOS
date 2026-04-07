'''Napíš program s funkciou 
slovenska_vlajka(x,
 
y,
 
sir,
 
vys,
 
modra='#0b4ea2',
 
cervena='#ee1c25')
, ktorá nakreslí 
vlajku Slovenska
. V súbore 
sk.png
 je obrázok štítu so znakom:






ktorý umiestniš (jeho stred) posunutý o ´´100´´ a 
108
 od ľavého horného okraja vlajky. V parametroch 
x,
 
y,
 
sir,
 
vys
 je momentálna pozícia ľavého horného rohu, šírka a výška vlajky, modrá a červená farba. Pre volanie 
slovenska_vlajka(30,
 
30,
 
325,
 
216)
 by si mal dostať takýto výstup:






Premenná, v ktorej budete mať uložený obrázok (prečítaný pomocou 
tkinter.PhotoImage
), nemôže byť lokálnou premennou funkcie 
slovenska_vlajka
 (tomuto budeme rozumieť až neskôr). Preto do tejto premennej načítajte obrázok ešte pred volaním funkcie 
slovenska_vlajka
, napríklad za príkazom 
canvas.pack()
.
'''