'''odovzdaj
 Funkciu 
nsd(a,
 
b)
 (najväčší spoločný deliteľ) vieme zapísať rekurzívne takto: triviálny prípad je vtedy, keď 
a==b
, inak ak 
a>b
, tak rekurzívne vypočíta 
nsd(b,
 
a)
, inak rekurzívne zavolá 
nsd(a,
 
b-a)
. Napríklad:


def
 
nsd
(
a
,
 
b
):

    
if
 
a
 
==
 
b
:

        
return
 
a

    
if
 
a
 
>
 
b
:

        
return
 
nsd
(
b
,
 
a
)

    
return
 
nsd
(
a
,
 
b
 
-
 
a
)






Funkcia 
nsd
 sa dá ale urýchliť tak, že namiesto odčitovania sa nejako využije zvyšok po delení. Oprav túto funkciu.
'''