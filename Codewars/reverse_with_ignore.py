def lis_rev(string, ignore):
    num_to_reverse = [i for i in string if i not in ignore][::-1]
    constants = list(enumerate(i for i in string if i in ignore))
    for j in range(len(constants)):
        num_to_reverse.insert(constants[j][0], constants[j][1])
    return "".join(num_to_reverse)


def rev(string, ignore):
    r = (i for i in string[::-1] if i not in ignore)
    return "".join(i if i in ignore else next(r) for i in string)


if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(100000):
        lis_rev("1234567890", "369")
    stop = time.time()
    print(stop-start)
    start = time.time()
    for i in range(100000):
        rev("1234567890", "369")
    stop = time.time()
    print(stop-start)
