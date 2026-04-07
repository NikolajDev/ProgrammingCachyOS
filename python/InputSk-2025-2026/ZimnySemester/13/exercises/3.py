'''Na predchádzajúcej prednáške sa riešíla trieda 
Cas
:


class
 
Cas
:


    
def
 
__init__
(
self
,
 
hodiny
=
0
,
 
minuty
=
0
,
 
sekundy
=
0
):

        
self
.
sek
 
=
 
abs
(
3600
 
*
 
hodiny
 
+
 
60
 
*
 
minuty
 
+
 
sekundy
)


    
def
 
__str__
(
self
):

        
return
 
f
'
{
self
.
sek
 
//
 
3600
}
:
{
self
.
sek
 
//
 
60
 
%
 
60
:
02
}
:
{
self
.
sek
 
%
 
60
:
02
}
'


    
def
 
sucet
(
self
,
 
iny
):

        
return
 
Cas
(
sekundy
=
self
.
sek
 
+
 
iny
.
sek
)


    
def
 
rozdiel
(
self
,
 
iny
):

        
return
 
Cas
(
sekundy
=
self
.
sek
 
-
 
iny
.
sek
)


    
def
 
vacsi
(
self
,
 
iny
):

        
return
 
self
.
sek
 
>
 
iny
.
sek






Podobne, ako v predchádzajúcej (2) úlohe, pridaj tri 
property
: 
hodiny
, 
minuty
 a 
sekundy
:




najprv atribút 
sek
 premenuj tak, aby začínal znakom podčiarkovník


pre každé z troch 
property
 zadefinuj zodpovedajúci 
getter
 v tvare 
daj_atribút()
 a 
setter
 v tvare 
zmen_atribut()


pomocou funkcie 
property(getter,
 
setter)
 zadefinuj všetky tri nové virtuálne atribúty




V triede nemeň už definované metódy


Malo by, napríklad, fungovať:


>>> 
c
 
=
 
Cas
(
8
,
 
35
,
 
40
)


>>> 
print
(
c
.
hodiny
,
 
c
.
minuty
,
 
c
.
sekundy
)


    8 35 40


>>> 
c
.
minuty
 
=
 
53


>>> 
print
(
c
)


    8:53:40


>>> 
c
.
hodiny
 
=
 
12


>>> 
print
(
c
)


    12:53:40


>>> 
c
.
sekundy
 
=
 
27


>>> 
print
(
c
)


    12:53:27
'''