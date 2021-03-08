import random

list = ["pies", "kot", "ptak", "owad", "ryba"]

for i in range(len(list)):
    word = random.choice(list)
    print(word)
    del list[list.index(word)]