import pathlib

import pytest

from rshanker779_common.profiler import Profiler


@pytest.fixture
def example_function():
    def example_string_function(x, y):
        return str(reversed(x)) + y

    return example_string_function


def test_profiler(example_function):
    profiler = Profiler(
        example_function, num_iterations=100, x="xfsjkfljkslf", y="fkdskfl"
    )
    profiler.profile()
    assert pathlib.Path(profiler.filename).is_file()


def test_profiler_estimation(example_function):
    profiler = Profiler(example_function, "afdjkla", "dsajdknsa")
    profiler.profile()
    assert profiler.num_iterations > 10_000
    assert profiler.num_iterations < 1_000_000
