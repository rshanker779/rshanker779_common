import os
import time


def get_reformatted_headers(filepath):
    header_dict = {}
    with open(filepath, 'r') as f:
        for row in f:
            header_dict[row.split(':')[0]] = row.split(':')[-1]
    return header_dict


def make_dirs(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def time_it(f):
    def wrapper_func(*args, **kwargs):
        s = time.perf_counter()
        f(*args, **kwargs)
        elapsed = time.perf_counter() - s
        print(f"{f.__name__} exectuted in {elapsed:2f} seconds")
    return wrapper_func


if __name__ == '__main__':
    x = get_reformatted_headers(os.path.join('espn_golf', 'headers.txt'))
    print()
