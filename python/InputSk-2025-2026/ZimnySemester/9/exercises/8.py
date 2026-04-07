'''odovzdaj
 Napíš rekurzívnu funkciu 
palindrom(retazec)
, ktorá zistí (vráti 
True
 alebo 
False
), či je zadaný reťazec 
palindróm
, t.j. či sa číta rovnako od začiatku ako od konca. Pri tomto zisťovaní sa nerozlišujú malé a veľké písmená, napríklad:


>>> 
palindrom
(
'JelenoviPivoNelej'
)


    True






Rekurzia by mala pracovať na takomto princípe: porovná prvé a posledné písmeno a ak sú zhodné ešte zistí, či aj reťazec bez prvého a posledného písmena je palindróm:




triviálny prípad: reťazec je prázdny alebo jednoznakový => 
True


inak: musia sa zhodovoť prvý a posledný znak a tiež zvyšok reťazca (okrem prvého a posledného) je palindróm (rekurzívne volanie)
'''