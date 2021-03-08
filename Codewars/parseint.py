#  converts string numbers to int


def parse_int(string):
    numbers = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    multiples = {"hundred": 100, "thousand": 1000, "million": 1000000}

    stack = string.replace("-", " ").replace(" and ", " ").split()
    rep = 0

    for i, s in enumerate(stack):
        if s in numbers:
            rep += numbers[s]
        else:
            if s == "hundred":
                rep += numbers[stack[i - 1]] * multiples[s] - numbers[stack[i - 1]]
            else:
                rep *= multiples[s]

    return rep


print(parse_int('six hundred sixty-six thousand six hundred sixty-six'), 666666)
