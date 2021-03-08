def pied_piper(string):
    rats = {0: "O~", 1: "~O"}
    direction = 0
    stack = ""
    deaf = 0
    for s in string.replace(" ", ""):
        if s == "P":
            direction = 1
            continue
        stack = stack + s
        if stack == rats[direction]:
            deaf += 1
            stack = ""
        elif len(stack) == 2:
            stack = ""
    return deaf


def pied_piper1(string):
    return string.replace(" ", "")[::2].count("O")


print(pied_piper("~O~O~O~O P"), 0)
print(pied_piper("P O~ O~ ~O O~"), 1)
print(pied_piper("~O~O~O~OP~O~OO~"), 2)
print(pied_piper1("~O~O~O~O P"), 0)
print(pied_piper1("P O~ O~ ~O O~"), 1)
print(pied_piper1("~O~O~O~OP~O~OO~"), 2)
