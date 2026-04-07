'''Vypíš obsah textového súboru do grafickej plochy. Súbor obsahuje niekoľko riadkov a funkcia 
vykresli_text(meno_suboru,
 
velkost=16)
 tieto riadky vypíše pod sebou fontom 
'consolas'
 (alebo podobným) a velkosťou fontu danou parametrom 
velkost
. V globálnej premennej 
canvas
 je referencia na grafickú plochu. Napríklad pre súbor 
'text3.txt'
 volanie:


>>> 
vykresli_text
(
'text3.txt'
)






do grafickej plochy vypíše:


Pre zarovnanie vypisovaného textu pomocou 
create_text
 nie na stred ale na ľavý okraj môžeš použiť ďalší pomenovaný parameter 
anchor='nw'
, potom by si mal dostať takýto výpis:


>>> 
vykresli_text
(
'text3.txt'
,
 
20
)
'''