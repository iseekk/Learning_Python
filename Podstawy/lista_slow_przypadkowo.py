import random

l = ["pies", "kot", "ptak", "owad", "ryba"]

for i in range(len(l)):
    word = random.choice(l)
    print(word)
    del l[l.index(word)]
