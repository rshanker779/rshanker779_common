import time
from functools import wraps
from typing import Dict, Union

from rshanker779_common.logger import get_logger

logger = get_logger(__name__)


def get_reformatted_headers(filepath: Union[str, bytes]) -> Dict:
    """

    :param filepath:
    :return:
    """
    header_dict = {}
    with open(filepath, "r") as f:
        for row in f:
            header_dict[row.split(":")[0]] = row.split(":")[-1]
    return header_dict


def time_it(f):
    """

    :param f:
    :return:
    """

    @wraps(f)
    def wrapper_func(*args, **kwargs):
        s = time.perf_counter()
        f(*args, **kwargs)
        elapsed = time.perf_counter() - s
        logger.info(f"{f.__name__} exectuted in {elapsed:2f} seconds")

    return wrapper_func


if __name__ == "__main__":

    @time_it
    def test_function():
        time.sleep(0.5)

    def test_add_function(x, y):
        return str(reversed(x)) + y

    test_function()
