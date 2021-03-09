def timer(func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter() - t1
        print(f"{t2}")
        return result

    return wrapper


@timer
def fib(n):
    x, y = 1, 1
    for _ in range(n):
        yield x
        x, y = y, x + y


print(list(fib(100))[-1])
# try:
#     user_input = int(input("Enter an integer: "))
# except ValueError:
#     print("It is not an integer")
# else:
#     print(list(fib(user_input))[-1])
