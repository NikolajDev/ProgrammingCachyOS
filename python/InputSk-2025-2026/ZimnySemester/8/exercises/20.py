'''-
 Napíš dve funkcie 
vyrob(n,
 
poz)
 a 
smerom(zoznam,
 
poz)
:




prvá funkcia 
vyrob(n,
 
poz)
 vytvorí na náhodných pozíciách 
n
 korytnačiek, každej nastaví náhodnú farbu pera a hrúbku pera 
5
; každú korytnačku ešte natočí smerom k bodu 
poz
 (parameter 
poz
 je dvojica nejakých súradníc 
(x,
 
y)
); všetky tieto korytnačky vloží do zoznamu a tento zoznam vráti (
return
) ako výsledok funkcie; zrejme využiješ korytnačiu metódu 
towards


druhá funkcia 
smerom(zoznam,
 
poz)
 dostáva zoznam korytnačiek a nechá postupne všetky korytnačky z tohto zoznamu presúvať k bodu 
poz
 tak, že 50-krát robí toto:




každá korytnačka si vypočíta vzdialenosť k bodu 
poz
 a prejde (
forward
) desatinu tejto vzdialenosti








Otestuj, napríklad:


pp
 
=
 
(
0
,
 
-
300
)


zoz
 
=
 
vyrob
(
100
,
 
pp
)


smerom
(
zoz
,
 
pp
)
'''