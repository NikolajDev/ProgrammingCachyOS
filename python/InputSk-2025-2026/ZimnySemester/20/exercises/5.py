'''-
 Napíš funkciu 
kopia(obrazok)
, ktorá vyrobí kópiu pôvodného obrázka, ale tak, že ho kopíruje po jednom pixeli. Zrejme si najprv vytvoríš prázdny obrázok rovnakých rozmerov a sem budeš kopírovať pixely (pomocou 
getpixel()
 a 
putpixel()
). Funkcia vráti tento nový obrázok ako svoj výsledok. Teraz prečítaj nejaký malý obrázok zo súboru a vyrob z neho pomocou 
kopia()
 kópiu (pre veľké obrázky to môže dosť dlho trvať).  Výsledok ulož do súboru a skontroluj. Napríklad:


>>> 
kopia
(
Image
.
open
(
'tiger.png'
))
.
show
()
'''