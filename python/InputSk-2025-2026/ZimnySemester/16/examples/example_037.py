>>> def fun2(x): return 2 * x + 1
>>> def fun3(x): return x // 2
>>> zoznam = [fun1, fun2, fun3]
>>> for f in zoznam:
...     print(f(10))
    100
    21
    5