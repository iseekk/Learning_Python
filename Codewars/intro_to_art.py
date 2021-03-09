from time import time


def get_w1(height):
    if height < 2: return []
    outcome = [""] * height
    for i in range(len(outcome)):
        outcome[i] += "*" if not i else " "
    last = 0
    for i in range(2):
        for j in range(height - 1):
            inserted = False
            for index, verse in enumerate(outcome):
                if index - 1 == last and not inserted:
                    outcome[index] += "*"
                    last += 1
                    inserted = True
                else:
                    outcome[index] += " "
        for k in range(height - 1):
            inserted = False
            for index, verse in enumerate(outcome):
                if index + 1 == last and not inserted:
                    outcome[index] += "*"
                    last -= 1
                    inserted = True
                else:
                    outcome[index] += " "
    return outcome


def get_w(height):
    lines = [(i * " " + "*").ljust(height) for i in range(height)]
    return [a + b[1:] + a[1:] + b[1:] for a, b in zip(lines, reversed(lines))]


s = time()
for i in range(10000):
    get_w1(10)
print(time() - s)
