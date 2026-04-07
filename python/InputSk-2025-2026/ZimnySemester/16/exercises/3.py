'''-
 Napíš funkciu 
zadaj(text)
, ktorá si najprv so zadaným textom vypýta nejaký vstup (
input()
) a potom ho prerobí na zoznam celých čísel. V prípade chyby nespadne, ale vráti prázdny zoznam. Napríklad:


>>> 
zoz
 
=
 
zadaj
(
'zadaj cisla: '
)


    zadaj cisla: 6 73 -8


>>> 
zoz


    [6, 73, -8]


>>> 
zoz
 
=
 
zadaj
(
'zadaj: '
)


    zadaj: 6 73 a -8


>>> 
zoz


    []






Úlohu vyrieš takouto schémou funkcie (nepridávaj ďalšie riadky):


def
 
zadaj
(
text
):

    
try
:

        
return
 
...

    
except
 
...
:

        
return
 
...
'''