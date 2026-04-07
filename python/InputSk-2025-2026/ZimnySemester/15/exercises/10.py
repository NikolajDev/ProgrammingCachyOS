'''-
 Do súboru 
struktury.py
 pridaj aj definíciu triedy  
Queue
 z prednášky. Podobne ako pri 
Stack
 do 
__init__
 pridaj nepovinný parameter 
postupnost
 a dopíš magickú metódu 
__repr__
:


class
 
Queue
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
 
'Queue(...)'






Otestuj:


>>> 
from
 
struktury
 
import
 
Queue


>>> 
Queue
(
range
(
5
))


    Queue((0, 1, 2, 3, 4))


>>> 
Queue
([
123
])


    Queue((123,))


>>> 
Queue
([])


    Queue()
'''