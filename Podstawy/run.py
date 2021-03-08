w = 5
for i in range(1, w+1):
    print(" ".join(str(2**i*j) for j in range(1, i+1)))

print("\n".join(" ".join(str(2**i*j) for j in range(1, i+1)) for i in range(1, w+1)))