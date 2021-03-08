from collections import Counter

puzzle = "367479-893698".split("-")
min, max = int(puzzle[0]), int(puzzle[1]) + 1

result = 0

for n in range(min, max):
    c = Counter(str(n))
    if 2 in c.values():
        numbers = [int(i) for i in str(n)]

        for i, num in enumerate(numbers[:-1]):
            if num > numbers[i+1]:
                break
        else:
            result += 1

print(result)
