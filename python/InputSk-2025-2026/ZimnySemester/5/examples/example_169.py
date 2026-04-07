>>> def cs(n):
...     vysl = 0
...     for znak in str(n):
...         vysl += int(znak)
...     return vysl
>>> vysl = []
>>> for i in range(100):
...     if cs(i) == 5:
...         vysl.append(i)
>>> vysl
    [5, 14, 23, 32, 41, 50]