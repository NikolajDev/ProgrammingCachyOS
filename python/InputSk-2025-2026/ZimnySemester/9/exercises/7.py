'''odovzdaj
 Napíš rekurzívnu funkciu 
mocnina(n,
 
k)
, ktorá vypočíta 
n**k
 pre celé nezáporné 
k
 len pomocou násobenia:




mocnina(n,
 
0)
 = 1


mocnina(n,
 
k)
 = 
mocnina(n,
 
k-1)
 
*
 
n




Funkcia, napríklad:


def
 
mocnina
(
n
,
 
k
):

    
if
 
k
 
==
 
0
:

        
return
 
1

    
return
 
n
 
*
 
mocnina
(
n
,
 
k
 
-
 
1
)



print
(
mocnina
(
2
,
 
900
)
 
==
 
2
 
**
 
900
)






Keďže nefunguje volanie 
mocnina(2,
 
10000)
, vylepši túto funkcie podľa tohto rekurzívneho predpisu:




mocnina(n,
 
0)
 = 1


mocnina(n,
 
k)
 = 
mocnina(n,
 
k//2)
 
**
 
2
 … pre párne 
k


mocnina(n,
 
k)
 = 
mocnina(n,
 
k-1)
 
*
 
n
 … pre nepárne 
k




Využíva sa tu umocňovanie na 
2
, čo je opäť len násobením dvoch čísel.
'''