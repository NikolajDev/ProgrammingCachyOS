def gg(*zoznam):
    return (i for i in range(20) if i % 7 in zoznam)