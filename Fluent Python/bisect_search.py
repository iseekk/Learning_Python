import bisect

a = [1, 4, 5, 6, 8, 12, 15, 20, 25, 30, 33, 41, 50]
b = [0, 1, 2, 5, 8, 10, 13, 19, 21, 40, 42, 55]

FRMT = "{0:2d} @ {1:2d}    {2:}{0:>2d}"

print("---------->", " ".join("%2s" % i for i in a))

for i in reversed(b):
    bisect_fn = bisect.bisect
    position = bisect_fn(a, i)
    offset = position * "  |"
    print(FRMT.format(i, position, offset))