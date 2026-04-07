'''Napíš funkciu 
prevrat(meno_suboru)
, ktorá prevráti poradie riadkov v danom textovom súbore. Funkcia nič nevypisuje ani nevracia, len zmení obsah zadaného textového súboru. Napríklad:


>>> 
print
(
'prvy
\n
 druhy
\n
  treti
\n
stvrty'
,
 
file
=
open
(
'text.txt'
,
 
'w'
))


>>> 
prevrat
(
'text.txt'
)


>>> 
print
(
open
(
'text.txt'
)
.
read
(),
 
end
=
''
)


    stvrty


      treti


     druhy


    prvy


>>>
'''