'''-
 Zadefinuj triedu 
Subor
 s metódami:




inicializácia
 
__init__(meno_suboru)
 vytvorí nový prázdny súbor


metóda
 
pripis(text)
 na koniec súboru pridá nový riadok so zadaným textom; použi 
open(...,
 
'a')


metóda
 
vypis()
 vypíše (
print
) momentálny obsah súboru




Napríklad test:


s
 
=
 
Subor
(
'text.txt'
)


s
.
pripis
(
'prvy riadok'
)


s
.
pripis
(
'druhy riadok'
)


s
.
vypis
()


s
.
pripis
(
'posledny riadok'
)


print
(
'***'
)


s
.
vypis
()






vypíše


prvy
 
riadok


druhy
 
riadok


***


prvy
 
riadok


druhy
 
riadok


posledny
 
riadok
'''