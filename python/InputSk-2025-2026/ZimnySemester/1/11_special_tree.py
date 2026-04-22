"""
Napíš program, ktorý z hviezdičiek vytvorí takúto pyramídu:

    v prvom riadku je najprv n-1 medzier a potom jedna hviezdička

    v každom ďalšom riadku je o jednu medzeru menej a o dve hviezdičky viac

Môžeš dostať takýto výstup:

zadaj n: 7
      *
     ***
    *****
   *******
  *********
 ***********
*************

Teraz napíš vylepšený variant predchádzajúcej úlohy: vytvorí pyramídu z hviezdičiek, len z hviezdičiek bude len obvod trojuholníka, vnútro trojuholníka bude zo znakov mínus ('-'). Môžeš dostať takýto výstup:

zadaj n: 7
      *
     *-*
    *---*
   *-----*
  *-------*
 *---------*
*************
"""

# FIRST PART
n = int(input("enter n: "))
val = 1
space = n - 1
for i in range(n):
    print(" " * space + "*"*val)
    val += 2
    space -= 1

# SECOND PART

n = int(input("enter n: "))
val = 1
space = n - 1
final = n * 2 - 1
print(" "*space + "*" * val)
space -= 1
for i in range(n-2):
    print(" " * space + "*" + "_"*val + "*")
    val += 2
    space -= 1
print(" " * space + "*" * final)

