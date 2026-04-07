'''-
 Vytvor súbor 
struktury.py
 a prekopíruj do neho definíciu triedy 
Stack
 z prednášky. V ďalších úlohách budeš používať 
import
 z tohto súboru. Do inicializácie triedy 
Stack
 ešte pridaj nepovinný parameter 
postupnost
, ktorý označuje postupnosť hodnôt, ktorou sa inicializuje zásobník (použi metódu 
push()
). Pridaj ešte novú magickú metódu 
__repr__()
, ktorá vráti zoznam všetkých prvkov zásobníka tak, že dno je na začiatku a vrch je na konci zoznamu (zásobník sa pritom nezmení). Tento zoznam vráti v tvare 
'Stack(...prvky...)'
, kde 
...prvky...
 sú vypísané ako n-tica (
tuple
). Dopíš:


class
 
Stack
:


    
def
 
__init__
(
self
,
 
postupnost
=
None
):


        
...

    
...

    
def
 
__repr__
(
self
):

        
return
 
'Stack(...)'






Otestuj:


>>> 
from
 
struktury
 
import
 
Stack


>>> 
Stack
(
range
(
5
))


    Stack((0, 1, 2, 3, 4))


>>> 
Stack
(
'Python'
)


    Stack(('P', 'y', 't', 'h', 'o', 'n'))


>>> 
Stack
([
123
])


    Stack((123,))


>>> 
Stack
()


    Stack()
'''