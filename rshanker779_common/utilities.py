import getpass
import os
import socket
import time
import datetime
from functools import wraps
from typing import Dict, Union, Callable
import cProfile
import subprocess
from rshanker779_common.logger import get_logger

logger = get_logger(__name__)


class Profiler:
    def __init__(self, function: Callable, num_iterations: int = 100, *args, **kwargs):
        """
        :param function: Ay function
        :param num_iteration: Number of calls to functio
        :param args: Any args for the callable
        :param kwargs: Any kwargs for the callable
        """
        self.raw_function = function
        self.num_iterations = num_iterations
        self.filename = None

        def func():
            for _ in range(self.num_iterations):
                function(*args, **kwargs)

        self.func = func

    def profile(self):
        filename = "{}_{}.prof".format(
            self.raw_function.__name__,
            datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S"),
        )
        self.filename = filename
        cProfile.runctx("self.func()", globals(), locals(), filename)

    def get_snakeviz_visualisation(self):
        # Note this requires snakeviz lib, but since it uses subprocess it's not an explicit dependency
        subprocess.call(["snakeviz", self.filename])


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


def make_dirs(directory: Union[str, bytes]) -> Union[str, bytes]:
    """

    :param directory:
    :return:
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def add_init_files(filepath: Union[str, bytes]):
    """

    :param filepath:
    :return:
    """
    for root, _, files in os.walk(filepath):
        # We need an init- if we have .py files, aren't in base dir (setup.py exists) and not already one
        needs_init_file = any(i for i in files if i.endswith(".py") and i != "setup.py")
        has_init_file = any(i for i in files if i == "__init__.py")
        if needs_init_file and not has_init_file:
            logger.info("Adding init file to directory %s", root)
            with open(os.path.join(root, "__init__.py"), "w") as f:
                pass


def get_hostname() -> str:
    """

    :return:
    """
    return socket.gethostname()


def get_username() -> str:
    """

    :return:
    """
    return getpass.getuser()




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
    x = get_hostname()
    y = get_username()
    add_init_files(os.path.join("/home/rohan/Documents/cellular-automata"))
    profiler = Profiler(test_add_function, 1000, "afdjsklfds", y="b")
    profiler.profile()
    profiler.get_snakeviz_visualisation()
    print()
