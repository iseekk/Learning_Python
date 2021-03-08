a = ["a", [4, 18], "b", [24, 25], "c", [17, 27], "d", [23, 22]]

b = re.index(regexp[a - z], a)

b = [0, 2, 4, 6]



ODPOWIEDŹ: [i for i, el in enumerate(a) if isinstance(el, str)]