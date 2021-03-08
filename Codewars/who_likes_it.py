def likes1(names):
    if len(names) >= 4:
        names = names[:2] + [f"{len(names) - 2} others"]
    return "{} like{} this".format(", ".join([n for n in names])[::-1].replace(",", "dna ", 1)[::-1] if names else "no one", "s" if len(names) < 2 else "")

def likes(names):
    output = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others likes this"
    }
    return output[min(4, len(names))].format(*names[:3], others=len(names))


import time
start = time.time()
for i in range(100000):
    likes1([])
    likes1(['Max', 'John', 'Mark'])
    likes1(['Max', 'John', 'Mark', 'Kate'])
print(time.time() - start)