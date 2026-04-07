'''-
 Nasledovná verzia triedenia vsúvaním 
insert_sort2()
 namiesto priraďovania do prvkov zoznamu používa metódy 
pop()
 a 
insert()
. Vlož do tejto funkcie kontrolné výpisy tak, ako sa to robilo na prednáške, a skontroluj jej spôsob triedenia:


def
 
insert_sort2
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


        
prvok
 
=
 
zoz
.
pop
(
i
)


        
j
 
=
 
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
 
prvok
:

            
j
 
-=
 
1


        
zoz
.
insert
(
j
+
1
,
 
prvok
)






Zamysli sa, prečo pre túto verziu nebude fungovať vizualizácia pomocou 
Vizualizuj
.


Odmeraj rýchlosť tohto triedenia v porovnaní s verziou z prednášky, vlož sem meranie času:


zoz
 
=
 
[
random
.
randrange
(
1000
)
 
for
 
i
 
in
 
range
(
5000
)]


zoz1
 
=
 
zoz
[:]


start
 
=
 
time
.
time
()


insert_sort
(
zoz
)


prvy_cas
 
=
 
...


start
 
=
 
time
.
time
()


insert_sort2
(
zoz1
)


druhy_cas
 
=
 
...


print
(
zoz
 
==
 
zoz1
,
 
prvy_cas
,
 
druhy_cas
)
'''