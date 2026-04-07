'''Triedenie 
insert sort
 môže byť zapísaný aj takto bez funkcie 
vymen
:


def
 
sort1
(
zoz
):

    
for
 
i
 
in
 
range
(
1
,
 
len
(
zoz
)):

        
t
,
 
j
 
=
 
zoz
[
i
],
 
i
 
-
 
1

        
while
 
j
 
>=
 
0
 
and
 
zoz
[
j
]
 
>
 
t
:

            
zoz
[
j
 
+
 
1
]
 
=
 
zoz
[
j
]

            
j
 
-=
 
1

        
zoz
[
j
 
+
 
1
]
 
=
 
t






Zisti, pre aký najväčší n-prvkový zoznam triedenie na tvojom počítači beží 1 sekundu, 2 sekundy a 3 sekundy. Zoznamy generuj s náhodnými hodnotami. Hľadanie takýchto 
n
 skús nejako zautomatizovať.
'''