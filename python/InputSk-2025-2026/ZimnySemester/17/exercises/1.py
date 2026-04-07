'''Napíš funkciu 
rozhadz(post)
, ktorá vráti pomiešaný zoznam prvkov vstupnej postupnosti. Funkcia by mala pracovať takto:




vstupnú postupnosť prerobí na zoznam


v cykle vyberie z tohto zoznamu náhodný prvok (
pop(index)
) a zaradí ho na koniec výsledného zoznamu (
append()
)


toto opakuje, kým nebude tento zoznam prázdny




Otestuj, napríklad:


>>> 
rozhadz
(
'abcdefghujkl'
)


    ['d', 'k', 'f', 'l', 'c', 'h', 'u', 'g', 'j', 'a', 'e', 'b']


>>> 
rozhadz
(
range
(
10
,
 
30
))


    [26, 29, 11, 23, 10, 12, 13, 21, 20, 27, 17, 16, 19, 22, 24, 15, 28, 18, 14, 25]






Teraz napíš testovaciu funkciu 
test(n)
, ktorá odmeria čas v sekundách trvania tejto funkcie 
rozhadz(range(n))
. Funkcia vráti tento čas zaokrúhlený na 3 desatinné miesta, napríklad:


>>> 
test
(
1000
)


    0.002


>>> 
test
(
10000
)


    0.027


>>> 
test
(
100000
)


    1.122






Zrejme na tvojom počítači dostaneš iné časy. Z modulu 
random
 použi len funkciu 
randrange
.
'''