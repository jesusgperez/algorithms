from logging import getLogger
from datetime import datetime

LOGGER = getLogger(__name__)

def measure_time(func):
    def wrapper(*args, **kw):
        start_time = datetime.now()
        result = func(*args, *kw)
        final_time = datetime.now() - start_time
        LOGGER.info(f'Function spent: {final_time}')
        return result

    wrapper.__name__ = func.__name__

    return func
