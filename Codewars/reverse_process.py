import re


def process(s, num):
    m = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    r = ""
    for c in s:
        x = num * m.index(c) % 26
        ch = m[x]
        r += ch
    result = str(num) + r
    return result


def decode(s):
    m = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    r = ""
    regex = re.match(r"^(\d+)([a-z]+)$", s)
    print(regex.group(1), regex.group(2))
    if regex:
        for char in regex.group(2):
            for i in range(26):
                if i * int(regex.group(1)) % 26 == m.index(char):
                    r += m[i]
                    break
            else:
                return "Impossible to decode"
        return r
    else:
        return "Impossible to decode"


print(process("qockcouoqmoayqwmkkic", 761328))
print(decode("761328qockcouoqmoayqwmkkic"), "Impossible to decode")