from enum import Enum


class Colors(Enum):
    black = 0
    brown = 1
    red = 2
    orange = 3
    yellow = 4
    green = 5
    blue = 6
    violet = 7
    gray = 8
    white = 9


def encode_resistor_colors(ohms_string):
    ohms = ohms_string[:-5].replace("k", "000").replace("M", "000000") if "." not in ohms_string \
        else ohms_string[:-5].replace("k", "00").replace("M", "00000").replace(".", "")
    return "{} {} {} gold".format(Colors(int(ohms[:1])).name, Colors(int(ohms[1:2])).name, Colors(int(len(ohms[2:]))).name)


# codes = 'black brown red orange yellow green blue violet gray white'.split()
# def encode_resistor_colors(ohms_string):
#     ohms = str(int(eval(ohms_string.replace(" ohms", "").replace("k", "*1000").replace("M", "*1000000"))))
#     return "{} {} {} gold".format(codes[int(ohms[0])], codes[int(ohms[1])], codes[len(ohms[2:])])


print(encode_resistor_colors("10 ohms"), "\nbrown black black gold")
print(encode_resistor_colors("47 ohms"), "\nyellow violet black gold")
print(encode_resistor_colors("100k ohms"), "\nbrown black yellow gold")
print(encode_resistor_colors("2M ohms"), "\nred black green gold")
print(encode_resistor_colors("4.7k ohms"), "\nyellow violet red gold")