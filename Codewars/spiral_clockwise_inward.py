def right(nums, x, y, matrix, times):
    for i in range(y + 1, y + 1 + times):
        if nums:
            if not matrix[x][i]:
                matrix[x][i] = nums.pop(0)
            else:
                times -= 1
                i -= 1
                break
    if nums:
        down(nums, x, i, matrix, times)


def down(nums, x, y, matrix, times):
    for i in range(x + 1, x + 1 + times):
        if nums:
            if not matrix[i][y]:
                matrix[i][y] = nums.pop(0)
            else:
                times -= 1
                i -= 1
                break
    if nums:
        left(nums, i, y, matrix, times)


def left(nums, x, y, matrix, times):
    for i in range(y - 1, y - 1 - times, -1):
        if nums:
            if not matrix[x][i]:
                matrix[x][i] = nums.pop(0)
            else:
                times -= 1
                i += 1
                break
    if nums:
        up(nums, x, i, matrix, times)


def up(nums, x, y, matrix, times):
    for i in range(x - 1, x - 1 - times, -1):
        if nums:
            if not matrix[i][y]:
                matrix[i][y] = nums.pop(0)
            else:
                times -= 1
                i += 1
                break
    if nums:
        right(nums, i, y, matrix, times)


def create_spiral(n):
    if not isinstance(n, int) or n < 1:
        return []
    else:
        nums = [_ for _ in range(1, n ** 2 + 1)]
        matrix = [[""] * n for _ in range(n)]
        matrix[0][0] = nums.pop(0)
        times = n - 1
        right(nums, 0, 0, matrix, times)
        return matrix


number = int(input("Wprowadź długość boku spirali: "))
while number > 0:
    for line in create_spiral(number):
        print(" ".join("{0:2d}".format(l) for l in line))
    number = int(input("Wprowadź długość boku spirali. Aby zakończyć, wprowadź liczbę 0: "))