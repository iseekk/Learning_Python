from collections import Counter


def letter_count(s):
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    return dict(sorted(d.items(), key=lambda x: x))


def letter_counter(s):
    c = Counter(s)
    return dict(sorted(dict(c).items()))


print(letter_count("codewars"))
print(letter_counter("codewars"))
