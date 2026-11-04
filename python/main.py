#elfs

with open("/home/nikolaj/ProgrammingCachyOS/python/elfs.txt", "r") as f:
    elfs = f.readlines()

for i in range(len(elfs)):
    elfs[i] = elfs[i].strip()

final_elfs = []
cals = 0
for elf in elfs:
    if elf == '':
        final_elfs.append(cals)
        cals = 0
    else:
        cals += int(elf)

final_elfs = sorted(final_elfs)
top_three = final_elfs[-1] + final_elfs[-2] + final_elfs[-3]
print(top_three)