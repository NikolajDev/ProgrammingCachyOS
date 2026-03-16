def base_check(n, base):
    n = n.lower()
    allchars = set()
    for i in range(base):
        allchars.add(str(i))
    if base > 10:
        for i in range(base - 10):
            allchars.add(str(chr(97 + i)))
    return set(allchars) >= set(n)


print(base_check("1055dsa", 13))
