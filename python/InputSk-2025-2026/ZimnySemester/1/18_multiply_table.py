"""Napíš program, ktorý vytvorí tabuľku násobenia, podobnú malej násobilke. Násobiť sa budú čísla z nejakého daného intervalu: v prvom riadku (aj stĺpci) sú násobky prvého čísla, v druhom druhého, atď. Môžeš dostať takýto výstup:

zadaj od: 8
zadaj do: 13
  64   72   80   88   96  104
  72   81   90   99  108  117
  80   90  100  110  120  130
  88   99  110  121  132  143
  96  108  120  132  144  156
 104  117  130  143  156  169

Do výpisu tabuľky pridaj prvý stĺpec aj riadok navyše s číslami z daného intervalu, napríklad v takomto tvare:

zadaj od: 8
zadaj do: 13
     |    8    9   10   11   12   13
=====|===============================
   8 |   64   72   80   88   96  104
   9 |   72   81   90   99  108  117
  10 |   80   90  100  110  120  130
  11 |   88   99  110  121  132  143
  12 |   96  108  120  132  144  156
  13 |  104  117  130  143  156  169

"""

# FIRST PART
start = int(input("zadaj od: "))
stop = int(input("zadaj do: "))
max_len = len(str(stop * stop))

for i in range(start, stop + 1):
    for j in range(start, stop + 1):
        print(f"{i*j:>{max_len}}", end="   ")
    print()

# SECOND PART
start = int(input("zadaj od: "))
stop = int(input("zadaj do: "))
max_len = len(str(stop * stop))

print(" " * max_len + " |", end="")
for j in range(start, stop + 1):
    print(f"{j:>{max_len+2}}", end=" ")
print()


print("=" * (max_len + 1) + "|" + "=" * ((max_len + 3) * (stop - start + 1)))

for i in range(start, stop + 1):
    print(f"{i:>{max_len}} |", end="")
    for j in range(start, stop + 1):
        print(f"{i*j:>{max_len+2}}", end=" ")
    print()
