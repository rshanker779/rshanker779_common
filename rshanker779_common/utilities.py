import os
import time
from functools import wraps
import socket
import getpass
from typing import Dict, Union
from rshanker779_common.logger import get_logger

logger = get_logger(__name__)


def get_reformatted_headers(filepath: Union[str, bytes]) -> Dict:
    header_dict = {}
    with open(filepath, "r") as f:
        for row in f:
            header_dict[row.split(":")[0]] = row.split(":")[-1]
    return header_dict


def make_dirs(directory: Union[str, bytes]) -> Union[str, bytes]:
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def add_init_files(filepath: Union[str, bytes]):
    for root, _, files in os.walk(filepath):
        # We need an init- if we have .py files, aren't in base dir (setup.py exists) and not already one
        needs_init_file = any(i for i in files if i.endswith(".py") and i != "setup.py")
        has_init_file = any(i for i in files if i == "__init__.py")
        if needs_init_file and not has_init_file:
            logger.info("Adding init file to directory %s", root)
            with open(os.path.join(root, "__init__.py"), "w") as f:
                pass


def get_hostname() -> str:
    return socket.gethostname()


def get_username() -> str:
    return getpass.getuser()


def save_to_database(*args, **kwargs):
    raise NotImplementedError


def get_data(*args, **kwargs):
    raise NotImplementedError


def time_it(f):
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

    test_function()
    x = get_hostname()
    y = get_username()
    add_init_files(os.path.join("/home/rohan/Documents/cellular-automata"))
    print()
