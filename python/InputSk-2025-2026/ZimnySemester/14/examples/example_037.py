>>> fun1()
    Traceback (most recent call last):
      File "<pyshell#9>", line 1, in <module>
        fun1()
      File "p.py", line 13, in fun1
        fun2()
      File "p.py", line 16, in fun2
        fun3()
      File "p.py", line 19, in fun3
        fun4()
      File "p.py", line 22, in fun4
        int('x')
    ValueError: invalid literal for int() with base 10: 'x'