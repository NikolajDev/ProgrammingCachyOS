'''Zadefinuj triedu 
VyrobPolygon
, ktorá bude fungovať takto:




metóda 
__init__(meno_suboru)
 si zapamätá meno súboru a vytvorí prázdny súbor s týmto menom (súbor zatvorí), vytvorí grafickú plochu (
self.canvas
) a v nej jeden polygón s jediným bodom (0, 0), s čiernym obrysom a bielym vnútrom; zároveň zviaže (
bind
) dve metódy 
self.klik
 a 
self.enter
 na udalosti kliknutia a stlačenie klávesu Enter (udalosť 
'<Return>'
 zviaž pomocou 
bind_all
); okrem toho vytvorí atribút 
zoznam
 s prázdnym obsahom


metóda 
klik(event)
 pridá do zoznamu 
self.zoznam
 kliknuté súradnice (nie ako dvojicu, ale dve celé čísla za sebou) a pomocou 
self.canvas.coords(...)
 zmení vykresľovaný polygón na obsah tohto zoznamu


metóda 
enter(event)
 zapíše momentálny obsah zoznamu (súradnice polygónu) na koniec súboru do jedného riadka ako postupnosť celých čísel oddelených medzerou; atribút zoznam potom vyprázdni a ďalšie klikania potom už vytvárajú nový polygón (opätovný Enter zapíše nový polygón ako ďalší riadok súboru)


keď bude táto trieda hotová, program naštartuj pomocou:




VyrobPolygon
(
'poly.txt'
)
    
# týmto sa zavolá konštruktor __init__()








naklikaj niekoľko polygónov a skontroluj obsah súboru
'''