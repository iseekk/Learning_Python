from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def prime_product(n):
    for i in range(n // 2, 1, -1):
        if (i == 2 or i % 2 != 0) and is_prime(i) and is_prime(n - i):
            return i * (n - i)
    return 0


if __name__ == "__main__":
    print(prime_product(20))
    import time
    for c in range(5):
        a = time.time()
        for i in range(99990, 100001):
            prime_product(i)
        print(time.time() - a)