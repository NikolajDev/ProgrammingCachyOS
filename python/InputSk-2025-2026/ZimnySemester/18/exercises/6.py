'''-
 Do všetkých funkcií 
bubble_sort()
, 
min_sort()
, 
insert_sort()
 a 
quick_sort()
 z prednášky dorob návratovú hodnotu, ktorou bude dvojica (počet porovnaní, počet výmen). Teda každá z funkcií vráti dve čísla: celkový počet porovnaní medzi prvkami zoznamu a celkový počet volaní funkcie 
vymen()
. Otestuj, napríklad takto:


zoz0
 
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



for
 
sort
 
in
 
bubble_sort
,
 
min_sort
,
 
insert_sort
,
 
quick_sort
:

    
zoz
 
=
 
list
(
zoz0
)

    
start
 
=
 
time
.
time
()

    
pp
,
 
pv
 
=
 
sort
(
zoz
)

    
cas
 
=
 
time
.
time
()
 
-
 
start

    
print
(
pp
,
 
pv
,
 
cas
)






Mal by si dostať štyri riadky výpisu - v každom je dvojica celých čísel a jedno desatinné číslo - zamysli sa, čo by si mohol z týchto čísel usúdiť.
'''