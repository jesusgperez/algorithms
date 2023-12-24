from logging import getLogger
from datetime import datetime

LOGGER = getLogger()


def measure_time(func):
    def wrapper(*args, **kw):
        start_time = datetime.now()
        result = func(*args, **kw)
        final_time = datetime.now() - start_time
        print(
            f'Function: {func.__name__} spent: {str(final_time.microseconds)}'
        )
        return result

    wrapper.__name__ = func.__name__
    return wrapper
