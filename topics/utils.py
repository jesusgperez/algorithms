from time import perf_counter
from typing import Callable

def measure_time(func: Callable):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(perf_counter() - start)
        return result
    wrapper.__name__ = func.__name__
    return wrapper

