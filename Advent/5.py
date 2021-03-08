program = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 10, 23, 1, 23, 6, 27, 1, 6, 27, 31, 1, 13, 31,
           35, 1, 13, 35, 39, 1, 39, 13, 43, 2, 43, 9, 47, 2, 6, 47, 51, 1, 51, 9, 55, 1, 55, 9, 59, 1, 59, 6, 63, 1, 9, 63,
           67, 2, 67, 10, 71, 2, 71, 13, 75, 1, 10, 75, 79, 2, 10, 79, 83, 1, 83, 6, 87, 2, 87, 10, 91, 1, 91, 6, 95, 1, 95,
           13, 99, 1, 99, 13, 103, 2, 103, 9, 107, 2, 107, 10, 111, 1, 5, 111, 115, 2, 115, 9, 119, 1, 5, 119, 123, 1, 123, 9,
           127, 1, 127, 2, 131, 1, 5, 131, 0, 99, 2, 0, 14, 0]


def computer(p):
    input_variable = p.pop(0)
    skip = 0
    for i, n in enumerate(p):
        if skip:
            skip -= 1
            continue
        elif n == 1:
            p[p[i + 3]] = p[p[i + 1]] + p[p[i + 2]]
            skip += 3
        elif n == 2:
            p[p[i + 3]] = p[p[i + 1]] * p[p[i + 2]]
            skip += 3
        elif n == 3:
            p[p[i + 1]] = input_variable
            skip += 1
        elif n == 4:
            output_value = p[p[i + 1]]
        elif n == 99:
            break
        skip += 3
    return p[0]


for i in range(100):
    for j in range(100):
        pr = program[:]
        pr[1] = i
        pr[2] = j
        result = computer(pr)
        if result == 19690720:
            print(100 * i + j)