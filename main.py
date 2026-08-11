from itertools import filterfalse

data = [10, 85, 300, 45, 500]

def expensive_check(n):
    print(f"Evaluating: {n}")
    return n > 100

lazy_stream = filterfalse(expensive_check, data)

first_match = next(lazy_stream)
print(f"Result: {first_match}")