from string import ascii_lowercase


def vowel_back(st):
    alphabet = ascii_lowercase * 3
    exceptions = "code"
    arr = ""
    for letter in st:
        i = alphabet.index(letter, 25)
        if letter in "aiu":
            new_letter = alphabet[i - 5]
        elif letter in "co":
            new_letter = alphabet[i - 1]
        elif letter == "d":
            new_letter = alphabet[i - 3]
        elif letter == "e":
            new_letter = alphabet[i - 4]
        else:
            new_letter = alphabet[i + 9]
        arr += new_letter if new_letter not in exceptions else letter
    return arr
