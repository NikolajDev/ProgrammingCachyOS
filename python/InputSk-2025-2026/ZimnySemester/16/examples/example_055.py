iterator = iter(zoznam)
while True:
    try:
        i = next(iterator)
        print(i, i * i)        # telo cyklu
    except StopIteration:
        break