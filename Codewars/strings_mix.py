from collections import Counter


def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    r = []
    for c in set(c1 | c2):
        if c1[c] > 1 or c2[c] > 1:
            if c1[c] > c2[c]:
                r.append("1:{}".format(c*c1[c]))
            elif c1[c] < c2[c]:
                r.append("2:{}".format(c*c2[c]))
            else:
                r.append("=:{}".format(c*c1[c]))
    return "/".join(sorted(r, key=lambda x: (-len(x), x)))


def mix1(s1, s2):
    o1 = Counter(filter(str.islower, s1))
    o2 = Counter(filter(str.islower, s2))
    result = {}
    for c in o1:
        if o1[c] > 1:
              result[c] = (o1[c], 1)
    for c in o2:
        if o2[c] > 1:
            if c in result:
                result[c] = (o2[c], 2) if result[c][0] < o2[c] else (o2[c], "=") if result[c][0] == o2[c] else result[c]
            else:
                result[c] = (o2[c], 2)
    result = ["{}:{}".format(item[1][1],item[0]*item[1][0]) for item in result.items()]
    result.sort(key=lambda x: (-len(x),x), reverse=False)
    return "/".join(result)


if __name__ == '__main__':

    print(mix("ala ma kota, a kot ma alę", "szafa tańczy o północy"))


# import time
#
# start = time.time()
# for i in range(50000):
#     mix("Are they here", "yes, they are here")
# end = time.time()
# print("isek:", end-start)
# start = time.time()
# for i in range(50000):
#     mix1("Are they here", "yes, they are here")
# end = time.time()
# print("Zosiek:", end-start)
