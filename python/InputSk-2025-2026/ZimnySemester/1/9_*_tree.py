"""
Napíš program, ktorý zo znakov hviezdička ('*') vytvorí takýto trojuholník: v 1. riadku je jedna hviezdička, v 2. dve, v 3. tri, …, v n-tom riadku je n hviezdičiek. Môžeš dostať takýto výstup:

zadaj n: 6
*
**
***
****
*****
******
"""

number = int(input("Enter the number of stars: "))
for i in range(1, number+1):
    print("*" * i)
