from functools import wraps
import time

from rshanker779_common import get_logger

logger = get_logger(__name__)


def time_it(f):
    @wraps(f)
    def wrapper_func(*args, **kwargs):
        s = time.perf_counter()
        res = f(*args, **kwargs)
        elapsed = time.perf_counter() - s
        logger.info(f"{f.__name__} executed in {elapsed:2f} seconds")
        return res

    return wrapper_func
