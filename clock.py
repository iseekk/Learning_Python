import time
import functools


def clock(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list += [str(arg) for arg in args]
        if kwargs:
            arg_list += [f"{k}={v}" for k, v in kwargs.items()]
        arg_str = ", ".join(arg_list)
        print(f"*** {name}({arg_str}) ran in {elapsed:.7f}s ***")
        return result
    return inner
