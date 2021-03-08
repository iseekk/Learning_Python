from operator import mul
from functools import reduce


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(mul, [int(x) for x in str(n)], 1)
        i += 1
    return i


print(persistence(39))
print(persistence(999))
print(persistence(25))
print(persistence(4))