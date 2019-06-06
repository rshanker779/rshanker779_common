import os
import time
from functools import wraps
import socket
import getpass
from typing import Dict, Union


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
        print(f"{f.__name__} exectuted in {elapsed:2f} seconds")

    return wrapper_func


if __name__ == "__main__":
    x = get_hostname()
    y = get_username()
    x = get_reformatted_headers(os.path.join("espn_golf", "headers.txt"))
    print()
