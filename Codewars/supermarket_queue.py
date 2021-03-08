def queue(customers, tills_num):
    tills = [0] * tills_num
    for c in customers:
        tills[0] += c
        tills.sort()
    return max(tills)


print(queue([1, 2, 10], 2))