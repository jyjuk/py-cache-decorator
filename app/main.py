from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def inner(*args) -> any:
        if args in cached_data:
            print("Getting from cache")
            return cached_data[args]
        else:
            print("Calculating new result")
            cached_data[args] = func(*args)
            return cached_data[args]

    return inner
