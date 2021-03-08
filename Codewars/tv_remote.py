def tv_remote(word):
    keyboard = [
        ["a", "b", "c", "d", "e", "1", "2", "3"],
        ["f", "g", "h", "i", "j", "4", "5", "6"],
        ["k", "l", "m", "n", "o", "7", "8", "9"],
        ["p", "q", "r", "s", "t", ".", "@", "0"],
        ["u", "v", "w", "x", "y", "z", "_", "/"],
    ]
    space = (5, 1)
    shift = (5, 0)
    uppercase = False
    pos = [(0, 0)]
    for letter in word:
        if letter == " ":
            pos.append(space)
        else:
            if letter.isalpha() and letter.isupper() != uppercase:
                pos.append(shift)
                uppercase ^= True
            for x, verse in enumerate(keyboard):
                if letter.lower() in verse:
                    y = verse.index(letter.lower())
                    pos.append((x, y))
    dist = []
    for i, c in enumerate(pos[:-1]):
        dist.append(abs(pos[i + 1][0] - c[0]) + abs(pos[i + 1][1] - c[1]) + 1)
    return sum(dist)


print(tv_remote("codewars"), 36)
print(tv_remote("Code Wars"), 69)
