'''-
 Napíš funkciu 
dom(d)
, ktorá nakreslí domček zo štvorca a rovnostranného trojuholníka tak, že po každej čiare prejde len raz. Pozícia korytnačky na obrázku je pri štarte. Po skončení kreslenia domčeka bude asi inde. Pre volanie 
dom(100)
 by si mal dostať:






Teraz napíš ďalšie dve funkcie 
prerusovana_ciara(d)
 a 
cikcakova_ciara(d)
, pomocou ktorých nakreslíme buď prerušovanú čiaru alebo cikcakovú čiaru. Prerušovaná čiara označuje rozdelenie úsečky dĺžky 
d
 na 
11
 rovnakoveľkých častí, pričom každá druhá sa prejde so zdvihnutým perom. Cikcaková čiara označuje, že úsečka dĺžky 
d
 sa rozdelí na úseky dĺžky 
5
 a každý úsek sa nakreslí pod uhlom 
60
 ako dve strany rovnostranného trojuholníka so stranou 
5
 (predpokladáme, že 
d
 je deliteľné číslom 
5
).


Ak by sme teraz vo funkcii 
dom
 nahradili volanie metódy 
t.fd(d)
 buď volaním 
prerusovana_ciara(d)
 alebo 
cikcakova_ciara(d)
, dostaneme domček z prerušovaných alebo cikcakových čiar:






Nepoužívaj metódu 
setpos
.
'''